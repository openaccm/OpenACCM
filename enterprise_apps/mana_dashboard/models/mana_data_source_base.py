# -*- coding: utf-8 -*-

from odoo import models, api, exceptions, _, tools
import json5, json
from odoo.tools.safe_eval import safe_eval, datetime, time, wrap_module, test_python_expr
from odoo.osv import expression
from box import Box
import math

default_json_data_key_val = """
[
      { product: 'Matcha Latte', '2015': 43.3, '2016': 85.8, '2017': 93.7 },
      { product: 'Milk Tea', '2015': 83.1, '2016': 73.4, '2017': 55.1 },
      { product: 'Cheese Cocoa', '2015': 86.4, '2016': 65.2, '2017': 82.5 },
      { product: 'Walnut Brownie', '2015': 72.4, '2016': 53.9, '2017': 39.1 }
]
"""

default_json_data_dimensions_datas = """
[
    ['product', '2015', '2016', '2017'],
    ['Matcha Latte', 43.3, 85.8, 93.7],
    ['Milk Tea', 83.1, 73.4, 55.1],
    ['Cheese Cocoa', 86.4, 65.2, 82.5],
    ['Walnut Brownie', 72.4, 53.9, 39.1]
]
"""


class ManaDataSourceMixin(models.Model):
    '''
    Mana Dashboard Data Source 
    '''
    _name = 'mana_dashboard.data_source_base'
    _description = 'Mana Dashboard Data Source Base'

    @api.model
    def get_data_from_sql(self, sql, extra_context = {}, get_field_infos = True):
        """
        get data from sql
        """
        if not sql:
            return {
                'datas': [],
                'field_infos': [],
            }
    
        # get data from sql
        try:

            eval_context = self._get_eval_context()
            eval_context.update(extra_context)
            if 'params' in eval_context:
                eval_context['params'] = Box(eval_context.get('params', {}))

            # replace ' to \'
            sql = sql.replace('\'', '\\\'')
            # replace " to \"
            sql = sql.replace('\"', '\\\"')
            # replace \n to \\n
            sql = sql.replace('\n', '\\\n')

            sql = 'result=f' + '\'' + sql + '\''

            try:
                code_obj = compile(sql, "", 'exec')
                eval(code_obj, eval_context)
                sql = eval_context.get('result')
            except Exception as e:
                return {
                    'datas': [],
                    'field_infos': [],
                    'error': 'Sql Error: %s' % e
                }
            sql = sql.strip()

            if not sql:
                raise exceptions.ValidationError(_('Sql Error: %s') % 'Sql is empty !!!')

            self.env.cr.execute(sql)
            datas = self.env.cr.dictfetchall()

            field_infos = []
            # get field infos
            for field in self.env.cr.description:
                type = field[1]
                # convert type integer to string
                if type == 23:
                    type = 'integer'
                elif type == 701:
                    type = 'float'
                elif type == 1082:
                    type = 'date'
                elif type == 1083:
                    type = 'time'
                elif type == 1114:
                    type = 'datetime'
                elif type == 16:
                    type = 'boolean'
                elif type == 1700:
                    type = 'float'
                elif type == 25:
                    type = 'text'
                elif type == 1043:
                    type = 'char'
                else:
                    type = 'other'

                field_infos.append({
                    'name': field[0],
                    'field_name': field[0],
                    'field': field[0],
                    'title': field[0],
                    'field_type': type,
                })
        except Exception as e:
            raise exceptions.ValidationError(_('Sql Error: %s') % e)

        return {
            'datas': datas,
            'field_infos': field_infos,
        }

    def get_data_source_info(self):
        """
        get data source info
        """
        self.ensure_one()

        data_source_type_name = self.data_source_type_name
        data_source_info = {
            'data_source_type_name': data_source_type_name,
            'result_type': self.result_type_name,
            'is_valid': False,
        }

        if data_source_type_name == 'model':
            data_source_info.update({
                'model_id': self.model.id,
                'model_name': self.model.model,
                'model': self.model.model,
                'domain': self.domain,
                'context': self.context,
                'model_fields': self.model_fields.read(),
                'group_by_infos': self.group_by_infos.read(),
                'order_by_infos': self.order_by_infos.read(),
                'raw_fields': self.raw_fields.read(),
                'limit': self.limit
            })
            if self.model:
                data_source_info['is_valid'] = True
        elif data_source_type_name == 'rpc':
            data_source_info.update({
                'method': self.method,
                'raw_fields': self.raw_fields.read(),
            })
            if self.model and self.method:
                data_source_info['is_valid'] = True
        elif data_source_type_name == 'sql':
            data_source_info.update({
                'sql': self.sql,
                'raw_fields': self.raw_fields.read(),
            })
            if self.sql:
                data_source_info['is_valid'] = True
        elif data_source_type_name == 'record':
            data_source_info.update({
                'res_id': self.res_id,
                'res_model': self.res_model,
            })
            if self.res_id and self.res_model:
                data_source_info['is_valid'] = True
        elif data_source_type_name == 'json':
            data_source_info.update({
                'json_data': self.json_data,
                'json_data_format': self.json_data_format,
                'raw_fields': self.raw_fields.read(),
            })
            if self.json_data:
                data_source_info['is_valid'] = True
        elif data_source_type_name == 'code':
            data_source_info.update({
                'code': self.code,
                'raw_fields': self.raw_fields.read(),
            })
            if self.code:
                data_source_info['is_valid'] = True

        # deal with the raw fields
        for raw_field in data_source_info.get('raw_fields', []):
            if raw_field['series_type']:
                raw_field['series_type'] = raw_field['series_type'][1]

        return data_source_info
    
    def is_all_fields_aggregates(self):
        """
        check if all fields are aggregates
        """
        self.ensure_one()
        return all([field.column_arggregation for field in self.raw_fields])

    @api.model
    def get_data_from_model(self, option, get_field_infos=True):
        """
        use the internal search_read method or the read_group method to get data
        """
        model_id = option.get('model_id')

        model = self.env['ir.model'].browse(model_id)
        domain = option.get('domain') 
        context = option.get('context')
        limit = option.get('limit', None)
        offset = option.get('offset', None)
        orderBy = option.get('orderBy', None)
        
        model_fields = option.get('model_fields', [])
        group_by_infos = option.get('group_by_infos', [])
        order_by_infos = option.get('order_by_infos', [])

        # get field infos
        field_infos = []
        name_cache = {} 
        if get_field_infos:
            for model_field in model_fields:
                title = model_field['field_description'] or model_field['field_name'] or model_field['full_name']
                name = model_field['field_name']
                if name_cache.get(name):
                    continue
                field_infos.append({
                    'field': name,
                    'field_name': name,
                    'field_type': model_field['field_type'],
                    'string': title,
                    'title': title,
                })
                name_cache[model_field['full_name']] = True

            # group by infos
            for group_by_info in group_by_infos:
                title = group_by_info['field_description'] or group_by_info['field_name'] or group_by_info['full_name']
                name = group_by_info['full_name']
                if name_cache.get(name):
                    continue
                field_infos.append({
                    'field': name,
                    'field_name': name,
                    'field_type': group_by_info['field_type'],
                    'string': title,
                    'title': title,
                })

            # order by infos
            # for order_by_info in order_by_infos:
            #     title = order_by_info['field_description'] or order_by_info['field_name'] or order_by_info['full_name']
            #     name = order_by_info['field_name']
            #     if name_cache.get(name):
            #         continue
            #     field_infos.append({
            #         'field': name,
            #         'field_name': name,
            #         'field_type': order_by_info['field_type'],
            #         'string': title,
            #         'title': title,
            #     })

        # get field names
        extra_field_ids = [
            group_by_info['field'] for group_by_info in group_by_infos if group_by_info['field']]
        extra_field_ids = extra_field_ids + [
            order_by_info['field'] for order_by_info in order_by_infos if order_by_info['field']]
        extra_fields = self.env['ir.model.fields'].browse(extra_field_ids)

        extra_fields_names = extra_fields.mapped('name')
        extra_fields_names = list(set(extra_fields_names))

        if group_by_infos:
            field_names = [model_field['full_name'] for model_field in model_fields if model_field['full_name']]
        else:
            field_names = [model_field['field_name'] for model_field in model_fields if model_field['full_name'] and model_field['field_name'] not in extra_fields_names]

        field_names = list(set(field_names))
        field_names = field_names + extra_fields_names

        if not model_id:
            return {
                'field_infos': field_infos,
                'datas': [],
            }

        # eval domain and context
        eval_context = self._get_eval_context()
        domain = domain or '[]'
        domain = safe_eval(domain.strip(), eval_context, mode="eval", nocopy=True)

        context = context or '{}'
        context = safe_eval(context.strip(), eval_context, mode="eval", nocopy=True)

        group_by_names = [group_by_info['full_name'] for group_by_info in group_by_infos if group_by_info['full_name']]
        group_by_names = list(set(group_by_names))
        order_by_names = [order_by_info['full_name'] for order_by_info in order_by_infos if order_by_info['full_name']]

        # check if all the fields has column aggregate
        if len(group_by_infos) > 0:
            if not get_field_infos and self.is_all_fields_aggregates():
                for field in self.raw_fields:
                    if field.column_arggregation:
                        group_by_names.append(field.full_name)

        order_by_names = list(set(order_by_names))
        if not orderBy:
            orderBy = ', '.join(order_by_names) if order_by_names else None

        if len(group_by_infos) > 0:
            datas = self.env[model.model].sudo().with_context(context).read_group(
                domain=domain,
                fields=field_names,
                groupby=group_by_names,
                orderby= orderBy,
                limit=limit,
                offset=offset,
                lazy=False)
        else:
            if len(field_names) == 0:
                field_names = ['id']
                field_infos.append({
                    'field': 'id',
                    'field_name': 'id',
                    'field_type': 'integer',
                    'string': 'id',
                    'title': 'id',
                })

            # use search to get data
            datas = self.env[model.model].sudo().with_context(context).search_read(
                domain=domain,
                fields=field_names,
                limit=limit,
                offset=offset,
                order=orderBy,
            )
        
        if len(group_by_infos) > 1:
            for record in datas:
                group_by_names = []
                for group_by_info in group_by_infos:
                    # check if is tuple or list
                    val = record[group_by_info['full_name']]
                    if isinstance(val, (tuple, list)):
                        val = f'{val[0]},{val[1]}'
                    group_by_names.append(str(val))
                record['__group_by_name'] = ' / '.join(group_by_names[1:])

        if len(datas) > 0 and get_field_infos:
            first_record = datas[0]
            keys = list(first_record.keys())
            for key in keys:
                if key not in field_names:
                    field_type = 'char'
                    if isinstance(first_record[key], (int)):
                        field_type = 'integer'
                    elif isinstance(first_record[key], (float)):
                        field_type = 'float'
                    else:
                        field_type = 'char'

                    field_infos.append({
                        'field': key,
                        'field_name': key,
                        'field_type': field_type,
                        'string': key,
                        'title': key,
                    })

        # deal field infos
        # if len(group_by_infos) == 0:
        for field_info in field_infos:
            if not field_info['field']:
                continue
            field_info['field'] = field_info['field'].split(':')[0]
            field_info['field_name'] = field_info['field_name'].split(':')[0]

        # remove id:count
        field_infos = [
            field_info for field_info in field_infos if field_info['field'] and field_info['field'] != 'id:count']

        # unique field infos
        field_infos = list({v['field']: v for v in field_infos}.values())

        return {
            'field_infos': field_infos,
            'datas': datas,
        }

    @api.model
    def get_data_from_model_method(self, model_id, method, extra_context, get_field_infos=True):
        """
        get data from model method
        """
        if not model_id or not method:
            return {
                'field_infos': [],
                'datas': [],
            }
        
        if 'params' not in extra_context:
            extra_context['params'] = Box(extra_context.get('params', {}))

        model = self.env['ir.model'].browse(model_id)
        datas = getattr(self.env[model.model], method)(extra_context)

        return {
            'field_infos': self._get_field_infos(datas, extra_context) if get_field_infos else [],
            'datas': datas,
        }
    
    @api.model
    def get_data_from_json(self, json_data, extra_context, get_field_infos=True):
        """
        get data from json
        """
        json_data_format = extra_context.get('json_data_format')
        if not json_data or not json_data_format:
            return {
                'field_infos': [],
                'datas': [],
            }

        datas = json5.loads(json_data or '[]')
        if json_data_format == 'dimensions_datas' and len(datas) > 0:
            names = datas[0]
            datas = datas[1:]
            datas = [dict(zip(names, data)) for data in datas]

        return {
            'field_infos': self._get_field_infos(datas, extra_context) if get_field_infos else [],
            'datas': datas,
        }
    
    @tools.ormcache()
    def get_custom_result_type(self):
        """
        get custom result type
        """
        return self.env.ref('mana_dashboard_base.result_type_custom')

    @api.model
    def get_data_from_code(self, code, extra_context={}, get_field_infos=True):
        """
        get data from python code
        """
        if not code:
            return {
                'datas': [],
                'field_infos': [],
            }

        eval_context = self._get_eval_context()
        eval_context.update(extra_context)
        if 'params' not in eval_context:
            eval_context['params'] = Box(eval_context.get('params', {}))

        safe_eval(code, eval_context, mode="exec", nocopy=True) 
        result = eval_context.get('result')

        return {
            'datas': result,
            'field_infos': self._get_field_infos(result, extra_context) if get_field_infos else [],
        }
    
    def _get_field_infos(self, results, result_type=None):
        """
        get field infos
        """
        field_infos = []
        # do not get result type for custom format data
        custom_result_type = self.get_custom_result_type()
        if not result_type:
            if self.result_type == custom_result_type:
                return field_infos
        else:
            if result_type == custom_result_type:
                return field_infos
        
        # check type
        if not isinstance(results, (list)):
            return field_infos
        
        if len(results) > 0:
            first_record = results[0]
            keys = list(first_record.keys())
            for key in keys:
                field_type = 'char'
                if isinstance(first_record[key], (int)):
                    field_type = 'integer'
                elif isinstance(first_record[key], (float)):
                    field_type = 'float'
                else:
                    field_type = 'char'

                field_infos.append({
                    'field': key,
                    'field_name': key,
                    'field_type': field_type,
                    'string': key,
                    'title': key,
                })

        return field_infos
    
    def get_extra_context(self, options={}):
        """
        get extra context
        """
        search_groups = options.get('search_group', [])
        context = {
            'search_groups': search_groups,
            'offset': options.get('offset', None),
            'limit': options.get('limit', None),
        }
        # mearge params value
        params_dict = self.parameter_ids.get_parameters()
        # update context to params
        for search_group in search_groups:
            for search_info in search_group:
                key = search_info.get('key')
                if not key:
                    continue
                type = search_info.get('type')
                if type == 'datetime_range':
                    params_dict[key] = {
                        'start': search_info.get('start'),
                        'end': search_info.get('end')
                    }
                else:
                    value = search_info.get('value')
                    params_dict[key] = value
                
        context['params'] = params_dict
        return context

    def _get_datas(self, options={}):
        """
        internal get data
        """
        data_source_type = self.data_source_type

        result = {
            'datas': [],
            'field_infos': [],
        }

        limit = options.get('limit', None)
        offset = options.get('offset', None)
        orderBy = options.get('order_by', [])
        
        # get data from data source type
        if data_source_type.name == 'model':

            if not options.get('fetch_model_data'):
                return result
            
            # cache all the field name
            field_names = {}
            for model_field in self.model_fields:
                field_names[model_field.field_name] = True
                
            for group_by_info in self.group_by_infos:
                if group_by_info.field:
                    field_names[group_by_info.field.name] = True

            for order_by_info in self.order_by_infos:
                if order_by_info.field:
                    field_names[order_by_info.field.name] = True
            
            model_id = self.model.id
            model_fields = self.model_fields.read()

            # get group by infos
            group_by_infos = self.group_by_infos.read()
            for group_by_info in group_by_infos:
                if group_by_info['field']:
                    group_by_info['field'] = group_by_info['field'][0]
            
            # get order by infos
            if orderBy:
                order_by_infos = orderBy
            else:
                order_by_infos = self.order_by_infos.read()
            for order_by_info in order_by_infos:
                if order_by_info['field']:
                    order_by_info['field'] = order_by_info['field'][0]

            domain = self.domain
            extra_context = self.context

            # append extra domain
            current_domain = domain or '[]'
            search_groups = options.get('search_groups', [])
            if search_groups:
                extra_domain = []
                for search_info in search_groups:
                    key = search_info.get('key')
                    if not key:
                        continue
                    value = search_info.get('value')
                    operator = search_info.get('operator', '=')
                    is_and = True if search_info.get('logic_type', 'and') == 'and' else False
                    type = search_info.get('type', 'char')
                    if key in field_names:
                        if type == 'datetime_range':
                            start = search_info.get('start')
                            end = search_info.get('end')
                            extra_domain = expression.AND(
                                [extra_domain, [(key, '>=', start), (key, '<=', end)]])
                        else:
                            if is_and:
                                extra_domain = expression.AND([extra_domain, [(key, operator, value)]])
                            else:
                                extra_domain = expression.OR([extra_domain, [(key, operator, value)]])

                if extra_domain:
                    extra_domain = str(extra_domain)
                    current_domain.strip()
                    if current_domain == '[]':
                        current_domain = extra_domain
                    else:
                        current_domain = current_domain[:-1] + ',' + extra_domain[1:]
                    current_domain.strip(',')

            has_drill_up = False
            if self.config_id:
                has_drill_up = self.config_id.drill_up_config != False
            else:
                has_drill_up = self.drill_up_config != False

            if has_drill_up and self.drill_domain:
                # append the drill up domain
                eval_ctx = dict(self.env.context)
                drill_domain = safe_eval(self.drill_domain, {
                    'context': eval_ctx
                })
                current_domain.strip()
                if current_domain == '[]':
                    current_domain = str(drill_domain)
                else:
                    current_domain = current_domain[:-1] + ',' + str(drill_domain)[1:]
                current_domain.strip(',')

            # linked action
            if self.env.context.get('$linked_field') \
                and self.env.context.get('$linked_value') \
                    and self.link_to_config \
                        and self.link_action_domain:
                # eval the linked action domain
                eval_ctx = dict(self.env.context)
                linked_action_domain = safe_eval(self.link_action_domain or '[]', {
                    'context': eval_ctx
                })
                current_domain.strip()
                if current_domain == '[]':
                    current_domain = str(linked_action_domain)
                else:
                    current_domain = current_domain[:-1] + ',' + str(linked_action_domain)[1:]
                current_domain.strip(',')

            if limit and self.limit:
                limit = min(self.limit, limit)
            elif self.limit:
                limit = self.limit
            
            # get data from model
            return self.get_data_from_model({
                'model_id': model_id,
                'domain': current_domain,
                'context': extra_context,
                'model_fields': model_fields,
                'limit': limit,
                'offset': offset,
                'group_by_infos': group_by_infos,
                'order_by_infos': order_by_infos,
            })
        elif data_source_type.name == 'sql':
            if not options.get('fetch_sql_data', True):
                return result
            extra_context = self.get_extra_context(options)
            return self.get_data_from_sql(self.sql, extra_context, get_field_infos = False)
        elif data_source_type.name == 'model_method':
            if not options.get('fetch_model_method_data', True):
                return result
            extra_context = self.get_extra_context(options)
            return self.get_data_from_model_method(extra_context, False)
        elif data_source_type.name == 'json':
            if not options.get('fetch_json_data', True):
                return result
            extra_context = self.get_extra_context(options)
            extra_context['json_data_format'] = self.json_data_format
            return self.get_data_from_json(self.json_data, extra_context, get_field_infos = False)
        elif data_source_type.name == 'code':
            if not options.get('fetch_code_data', True):
                return result
            extra_context = self.get_extra_context(options)
            return self.get_data_from_code(self.code, extra_context, get_field_infos = False)

    def _get_time_domain(self, options = {}):
        """
        get time domain
        """
        domains = []
        for field_info in self.model_fields:
            field_type = field_info.field.ttype
            if field_type == 'date' or field_type == 'datetime':
                
                # affect by global
                if field_info.affect_by_global:
                    start_time = options.get('start_time')
                    end_time = options.get('end_time')
                    if start_time and end_time:
                        domains.append((field_info.field_name, '>=', start_time))
                        domains.append((field_info.field_name, '<=', end_time))
                else:
                    if field_info.start_time and field_info.end_time:
                        start_time = field_info.start_time
                        end_time = field_info.end_time
                        if start_time:
                            domains.append((field_info.field_name, '>=', start_time))
                        if end_time:
                            domains.append((field_info.field_name, '<=', end_time))

        return domains
    
    def get_talbe_datas(self, options={}):
        """
        get table data
        """
        result = self._get_datas(options)
        return result.get('datas', [])

    def get_datas(self, options={}):
        """
        get data from data source, as we need to preview, so we can not get data from self
        """
        result = self._get_datas(options)
        data_source_info = self.get_data_source_info()

        # compute __group_by_name as model has computed
        if self.multi_group_by and self.data_source_type_name != 'model':
            group_by_names = []
            raw_fields = data_source_info.get('raw_fields')
            
            # get from raw fields
            for raw_field in raw_fields:
                if raw_field.get('group_by') and not raw_field.get('category'):
                    group_by_names.append(raw_field.get('field_name'))

            # compute __group_by_name
            datas = result.get('datas', [])
            for data in datas:
                group_by_name = ''
                for group_by_name in group_by_names:
                    group_by_name += str(data.get(group_by_name, '')) + '/'
                group_by_name = group_by_name[:-1]
                data['__group_by_name'] = group_by_name

        return {
            'data_source_info': data_source_info,
            'datas': result.get('datas', []) if result else [],
        }

    @api.model
    def get_test_data(self):
        """
        get test data from data source
        """
        data = [
            { 'product': 'Matcha Latte', '2015': 43.3, '2016': 85.8, '2017': 93.7 },
            { 'product': 'Milk Tea', '2015': 83.1, '2016': 73.4, '2017': 55.1 },
            { 'product': 'Cheese Cocoa', '2015': 86.4, '2016': 65.2, '2017': 82.5 },
            { 'product': 'Walnut Brownie', '2015': 72.4, '2016': 53.9, '2017': 39.1 }]
        
        return data
    
    def _get_eval_context(self):
        """
        Get the context used when evaluating python code
        """
        context = {
            # orm
            'env': self.env,
            'self': self,
            # Exceptions
            'Warning': exceptions.Warning,
            'UserError': exceptions.UserError,
            'datetime': datetime,
            'context_today': datetime.datetime.now,
            'user': self.env.user.with_context({}),
            'time': time,
            'res_company': self.env.company.sudo(),
            'json5': wrap_module(__import__('json5'), ['loads', 'dumps']),
            # import math functions
            'math': wrap_module(__import__('math'), ['sqrt', 'log', 'log10', 'log2', 'exp', 'expm1', 'log1p', 'cos', 'sin', 'tan', 'acos', 'asin', 'atan', 'atan2', 'hypot', 'degrees', 'radians', 'cosh', 'sinh', 'tanh', 'acosh', 'asinh', 'atanh', 'erf', 'erfc', 'gamma', 'lgamma', 'pi', 'e', 'tau', 'inf', 'nan', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'factorial', 'fmod', 'fsum', 'gcd', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'remainder', 'copysign', 'frexp', 'ldexp', 'modf', 'trunc', 'ceil', 'floor', 'fabs', 'factorial', 'fmod', 'fsum', 'gcd', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'remainder', 'copysign', 'frexp', 'ldexp', 'modf', 'trunc', 'ceil', 'floor', 'fabs', 'factorial', 'fmod', 'fsum', 'gcd', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'remainder', 'copysign', 'frexp', 'ldexp', 'modf', 'trunc', 'ceil', 'floor', 'fabs', 'factorial', 'fmod', 'fsum', 'gcd', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'remainder', 'copysign', 'frexp', 'ldexp', 'modf', 'trunc', 'ceil', 'floor', 'fabs', 'factorial', 'fmod', 'fsum', 'gcd', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'remainder', 'copysign', 'frexp', 'ldexp', 'modf', 'trunc', 'ceil', 'floor', 'fabs', 'factorial', 'fmod', 'fsum', 'gcd', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'remainder', 'copysign', 'frexp', 'ldexp', 'modf', 'trunc', 'ceil'])
        }

        return context
    
    def get_search_infos(self):
        """
        deprecated,
        get search infos from mana_dashboard.search_info, 
        """
        self.ensure_one()
        if self.config_id:
            dashboard_id = self.config_id.dashboard_id.id
        else:
            dashboard_id = self.dashboard_id.id

        any_config_id = self.config_id.any_config_id.id if self.config_id else self.any_config_id.id
        search_info_helper = self.env['mana_dashboard.search_info']\
            .get_search_info_helper(dashboard_id)

        if search_info_helper:
            search_infos = search_info_helper.get_search_infos(any_config_id)
            return search_infos
        else:
            return []

    def combine_raw_fields(self, raw_fields):
        """
        combine raw fields
        """
        if not raw_fields:
            return []
        
        # get old raw fields
        old_raw_fields = []
        for raw_field in self.raw_fields:
            old_raw_fields.append({
                'name': raw_field.name,
                'alias': raw_field.alias,
                'measure': raw_field.measure,
                'category': raw_field.category,
                'column_arggregation': raw_field.column_arggregation,
                'group_by': raw_field.group_by,
            })
        old_cache = {old_raw_field['name']: old_raw_field for old_raw_field in old_raw_fields}

        # update fields info
        for raw_field in raw_fields:
            if raw_field['field_name'] in old_cache:
                old_raw_field = old_cache[raw_field['field_name']]
                if old_raw_field['column_arggregation']:
                    raw_field['bottomCalc'] = old_raw_field['column_arggregation']
                else:
                    raw_field['bottomCalc'] = False

        return raw_fields
    
    def normalize_field_type(self, field_type):
        """
        normalize field type
        """
        if not field_type:
            return 'other'
        
        field_type = field_type.lower()
        if field_type == 'many2one':
            return 'integer'
        elif field_type == 'one2many':
            return 'array'
        elif field_type == 'many2many':
            return 'array'
        elif field_type == 'reference':
            return 'char'
        elif field_type == 'varchar':
            return 'char'
        elif field_type == 'text':
            return 'char'
        elif field_type not in ['char', 'integer', 'float', 'boolean', 'date', 'datetime', 'array']:
            return 'other'
        else:
            return field_type

    @api.onchange('fake_field')
    def onchange_fake_field(self):
        """
        when fake field changed, update fields
        """
        datas = self.fake_field
        if datas:
            columns = json.loads(datas)

            measure_fields = []
            if self.data_source_type.name == 'model':
                for model_field in self.model_fields:
                    if model_field.measure:
                        measure_fields.append(model_field.field_name)

            # as the data is in memory, so we can not get data by read
            old_raw_fields = []
            for raw_field in self.raw_fields:
                old_raw_fields.append({
                    'id': raw_field.id,
                    'name': raw_field.name, 
                    'type': raw_field.type,
                    'alias': raw_field.alias,
                    'measure': raw_field.measure,
                    'category': raw_field.category,
                    'column_arggregation': raw_field.column_arggregation,
                    'group_by': raw_field.group_by,
                    'supported_series_types': raw_field.supported_series_types,
                    'series_type': raw_field.series_type,
                })
            old_cache = {old_raw_field['name']: old_raw_field for old_raw_field in old_raw_fields}

            raw_fields = [(5, 0, 0)]
            for column in columns:
                vals = {}
                column_name = column.get('field_name')
                if column_name in old_cache:
                    vals = old_cache[column_name]
                else:
                    vals = {
                        'name': column_name,
                        'measure': False,
                        'category': False,
                        'type': self.normalize_field_type(column.get('field_type')),
                        # awesome, work with datasource mixin
                        'supported_series_types': self.config_id.supported_series_types.ids if self.config_id else self.supported_series_types.ids,
                    }

                if column_name in measure_fields:
                    vals['measure'] = True

                if self.group_by_infos:
                    if column.get('field_name') == self.group_by_infos[0].field.name:
                        vals['category'] = True
                        vals['measure'] = False
                        vals['group_by'] = True

                raw_fields.append((0, 0, vals))

            self.raw_fields = raw_fields

    @api.onchange('model')
    def onchange_model(self):
        """
        when model changed, update fields
        """
        self.group_by_infos = False
        self.order_by_infos = False
        self.model_fields = False
        self.raw_fields = False

    def do_query(self):
        """
        do query
        """
        if self.data_source_type.name == 'model':
            if not self.model:
                return []
            
            # avoid to get too many data
            if not self.model_fields \
                and not self.group_by_infos \
                    and not self.order_by_infos \
                        and not self.limit:
                raise exceptions.UserError(_('Please set model fields, group by, order by or limit!'))
            
        data_source = self.get_datas()
        return data_source

    def update_time_range_info(self, time_range_info):
        """
        update time range info
        """
        self.ensure_one()
        range_type = time_range_info.get('range_type')
        if not self.datetime_range:
            if range_type == 'Custom Range':
                self.datetime_range = self.env['mana_dashboard.datetime_range'].create({
                    'range_type': time_range_info.get('range_type')
                })
            else:
                self.datetime_range = self.env['mana_dashboard.datetime_range'].create({
                    'range_type': time_range_info.get('range_type'),
                    'custom_start_time': time_range_info.get('start_time'),
                    'custom_end_time': time_range_info.get('end_time'),
                })
        else:
            if range_type == 'Custom Range':
                self.datetime_range.write({
                    'range_type': time_range_info.get('range_type'),
                    'custom_start_time': False,
                    'custom_end_time': False,
                })
            else:
                self.datetime_range.write({
                    'range_type': time_range_info.get('range_type'),
                    'custom_start_time': time_range_info.get('start_time'),
                    'custom_end_time': time_range_info.get('end_time'),
                })

    @api.onchange('drill_field', 'drill_operator')
    def onchange_drill_info(self):
        """
        calc the drill down domain
        """
        self.ensure_one()
        if self.drill_field and self.drill_operator:
            self.drill_domain = f"[('{self.drill_field.name}', '{self.drill_operator}', context.get('$drill_field'))]"
        else:
            self.drill_domain = False

    @api.onchange('link_action_field', 'link_action_operator')
    def onchange_linked_info(self):
        """
        calc the link action domain linked_value
        """
        self.ensure_one()
        if self.link_action_field and self.link_action_operator:
            self.link_action_domain = \
                f"[('{self.link_action_field.name}', '{self.link_action_operator}', context.get('$linked_field'))]"
        else:
            self.link_action_domain = False

    @api.onchange('group_by_infos')
    def onchange_group_by_infos(self):
        """
        when group by infos changed, update fields
        """
        self.ensure_one()
        if self.group_by_infos:
            self.has_group_by = True
        else:
            self.has_group_by = False

    @api.onchange('model_fields')
    def onchange_model_fields(self):
        """
        when model fields changed, update fields
        """
        # has_time_field
        self.has_time_field = bool(self.model_fields.filtered(lambda x: x.show_time))

    @api.onchange('template_id')
    def onchange_template_id(self):
        """
        when template changed, update default_code
        """
        if self.template_id:
            if not self.code:
                self.code = self.template_id.default_code
                
            if not self.sql:
                self.sql = self.template_id.default_sql

            if not self.json_data:
                self.json_data = self.template_id.default_json

            if not self.demo_data:
                self.demo_data = self.template_id.demo_data
                
            # result_type
            self.result_type = self.template_id.default_result_type
            # data_source_type
            self.data_source_type = self.template_id.default_data_source_type

    @tools.ormcache()
    def _get_data_source_types(self):
        """
        get data source type
        """
        return self.env['mana_dashboard.data_source_type'].search([]).ids

    @tools.ormcache()
    def _get_result_types(self):
        return self.env['mana_dashboard.result_type'].search([]).ids

    @api.onchange('json_data_format')
    def onchange_json_data_format(self):
        """
        when json data format changed, update json data
        """
        if not self.json_data or self.json_data.strip() == '':
            if self.json_data_format == 'key_val':
                self.json_data = default_json_data_key_val
            else:
                self.json_data = default_json_data_dimensions_datas
        else:
            if self.json_data_format == 'key_val':
                json_data = json5.loads(self.json_data)
                if len(json_data) == 0:
                    return
                keys = json_data[0]
                for i in range(1, len(json_data)):
                    json_data[i] = dict(zip(keys, json_data[i]))
                # remove first line
                json_data = json_data[1:]
                self.json_data = json5.dumps(json_data, indent=4)
            else:
                # convert to dimensions_datas
                json_data = json5.loads(self.json_data)
                if len(json_data) == 0:
                    return
                keys = list(json_data[0].keys())
                json_data = [keys] + [[item[key] for key in keys] for item in json_data]
                self.json_data = json5.dumps(json_data, indent=4)
