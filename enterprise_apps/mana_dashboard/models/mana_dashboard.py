# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError
import json, json5
import re


class ManaDashboard(models.Model):
    '''
    Mana Dashboard
    '''
    _name = "mana_dashboard.dashboard"
    _description = "Mana Dashboard"
    _order = "id desc"

    name = fields.Char(string="Dashboard Name", required=True)
    use_template = fields.Boolean(string="Use Template", default=False)

    # template id 
    template_id = fields.Many2one(
        string="Template", 
        comodel_name='mana_dashboard.dashboard_template')
    template_inited = fields.Boolean(string="Template Inited", default=False)

    # files
    style_files = fields.Many2many(
        'ir.attachment', 
        string='Style Files', 
        relation='mana_dashboard_style_files_rel')   
    style_urls = fields.Text(string='Style Urls', compute='_compute_style_urls')
    js_files = fields.Many2many(
        'ir.attachment', 
        string='Js Files',
        relation='mana_dashboard_js_files_rel')
    js_urls = fields.Text(string='Js Urls', compute='_compute_js_urls')
    image_files = fields.Many2many(
        'ir.attachment', 
        string='Image Files',
        relation='mana_dashboard_image_files_rel')

    action_id = fields.Many2one(string="board action id", comodel_name='ir.actions.client')

    dashboard_html = fields.Text(string="Dashboard HTML")
    dashboard_css = fields.Text(string="Dashboard CSS")
    dashboard_js = fields.Text(string="Dashboard JS")

    custom_css = fields.Text(
        string="Dashboard CSS", help="This is custom css for dashboard")
    theme_info = fields.Text(
        string="Dashboard Theme", help="This is custom theme for dashboard")

    default_template_info = fields.Text(string="Default Template Info")

    config_ids = fields.One2many(
        string="Config Infos",
        comodel_name='mana_dashboard.any_config',
        inverse_name='dashboard_id')

    inited = fields.Boolean(string="Inited", default=False)
    binded_menu_count = fields.Integer(string="Binded Menu Count", compute='_compute_binded_menu_ids')
    binded_menu_ids = fields.One2many(
        string="Binded Menu",
        comodel_name='ir.ui.menu',
        compute='_compute_binded_menu_ids')
    
    active = fields.Boolean(string="Active", default=True)
    description = fields.Text(string="Description")

    operations = fields.Char(string="Operations", help="Operations for dashboard")

    # name must be unique
    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Dashboard name already exists !"),
    ]

    @api.model
    def create(self, vals):
        '''
        create the akl dashboard
        :param vals:
        :return:
        '''
        res = super(ManaDashboard, self).create(vals)

        if res.bind_to_menu and res.parent_menu_id:
            if not vals.get('action_id', False):
                val = {
                    'name': 'Dashboard_' + res.name,
                    'res_model': 'mana_dashboard.dashboard',
                    'params': {
                        'dashboard_id': res.id,
                        'mode': 'view'
                    },
                    'tag': 'mana_dashboard',
                }
                res.action_id = self.env['ir.actions.client'].sudo().create(val)
            else:
                res.action_id = vals.get('action_id')
                
            self.env['ir.ui.menu'].sudo().create({
                'name': res.menu_name,
                'parent_id': res.parent_menu_id.id,
                'sequence': res.menu_sequence,
                'action': "ir.actions.client," + str(res.action_id.id),
                'groups_id': [(6, 0, res.group_access_ids.ids)]
            })

        return res

    def unlink(self):
        '''
        unlink the dashboard
        :return:
        '''
        for rec in self:
            # search menu which bind to this dashboard
            records = self.env['ir.ui.menu'].sudo().search([
                ('action', '=', "ir.actions.client," + str(rec.action_id.id))
            ])
            records.sudo().unlink()
            rec.action_id.sudo().unlink()

        return super(ManaDashboard, self).unlink()

    def load_dashboard(self):
        """
        load dashboard 
        """
        self.ensure_one()
        result = self.read()[0]
        if result.get('style_urls', False):
            result['style_urls'] = json5.loads(result['style_urls'])
        if result.get('js_urls', False):
            result['js_urls'] = json5.loads(result['js_urls'])
        return result
    
    def reset_search_infos(self):
        '''
        reset search infos
        :return:
        '''
        self.ensure_one()
        self.env['mana_dashboard.search_info'].reset_search_infos(self.id)
        return True

    def _get_dashboard_action(self, mode):
        """
        get dashboard action
        """
        self.ensure_one()
        return {
            'name': 'Dashboard_' + self.name,
            "type": "ir.actions.client",
            "params": {
                "dashboard_id": self.id,
                "mode": mode
            },
            "tag": "mana_dashboard"
        }

    def edit_dashboard(self):
        '''
        edit dashboard
        :return:
        '''
        return self._get_dashboard_action('edit')

    def view_dashboard(self):
        '''
        view dashboard
        :return:
        '''
        return self._get_dashboard_action('view')

    def view_dashboard_full_screen(self):
        '''
        view dashboard full screen
        :return:
        '''
        action = self._get_dashboard_action('view')
        action['target'] = 'fullscreen'
        return action

    @api.model
    def get_model_field_statistics(self, model_id, field_id, statistics):
        """
        """
        ir_model = self.env['ir.model'].browse(int(model_id))
        field = self.env['ir.model.fields'].browse(int(field_id))
        if not ir_model or not field:
            return []
        domain = []
        
        if self.start_time:
            domain.append((field.name, '>=', self.start_time))
        if self.end_time:
            domain.append((field.name, '<=', self.end_time))

        # check the field type
        if statistics != 'count' and field.ttype not in ['integer', 'float']:
            raise UserError("Hi, Body, The field type is not integer or float!!!")

        model = self.env[ir_model.model].sudo()
        if statistics == 'count':
            return model.search_count(domain)
        elif statistics == 'sum':
            # check the field type
            if field.ttype not in ['integer', 'float']:
                raise UserError("Hi, Body, The field type is not integer or float!!!")
            records = model.search_read(domain, [field.name])
            return sum([record[field.name] for record in records])
        elif statistics == 'avg':
            records = model.search_read(domain, [field.name])
            if len(records) == 0:
                return []
            return sum([record[field.name] for record in records]) / len(records)
        elif statistics == 'min':
            records = model.search_read(domain, [field.name])
            return min([record[field.name] for record in records])  
        elif statistics == 'max':
            records = model.search_read(domain, [field.name])
            return max([record[field.name] for record in records])
        else:
            return []

    def update_search_infos(self, option):
        """
        update search info
        """
        uid = self.env.uid
        config_id = option.get('config_id', False)
        search_infos = option.get('search_infos', False)

        record = self.env['mana_dashboard.search_info'].search(
            [('uid', '=', uid), 
             ('dashboard_id', '=', self.id), 
             ('search_config_id', '=', config_id)])
        if record:
            record.search_infos = search_infos
        else:
            self.env['mana_dashboard.search_info'].create({
                'dashboard_id': self.id,
                'uid': uid,
                'search_infos': search_infos
            })
        # clear the cache
        self.env['mana_dashboard.search_info'].clear_caches()

    def bind_menu_wizard(self):
        """
        bind to menu
        """
        if not self.action_id:
            val = {
                'name': 'Dashboard_' + self.name,
                'res_model': 'mana.dashboard',
                'params': {
                    'dashboard_id': self.id,
                    'mode': 'view',
                },
                'tag': 'mana_dashboard',
            }
            action_id = self.env['ir.actions.client'].sudo().create(val)
            self.action_id = action_id

        return {
            "type": "ir.actions.act_window",
            "res_model": "mana_dashboard.bind_menu_wizard",
            "view_mode": "form",
            "target": "new",
            "context": {
                "default_action_id": self.action_id.id,
            }
        }

    @api.depends()
    def _compute_binded_menu_ids(self):
        """
        compute binded menu ids
        """
        for rec in self:
            rec.binded_menu_ids = self.env['ir.ui.menu'].sudo().search([
                ('action', '=', "ir.actions.client," + str(rec.action_id.id))
            ])
            rec.binded_menu_count = len(rec.binded_menu_ids)

    @api.model_create_multi
    @api.returns('self', lambda value: value.id)
    def create(self, vals_list):
        """
        update inited
        """
        records = super(ManaDashboard, self).create(vals_list)
        records.write({'inited': True})
        return records

    @api.onchange('template_id')
    def _onchange_template_id(self):
        """
        onchange template id
        """
        if self.template_id:
            self.style_files = self.template_id.style_files
            self.js_files = self.template_id.js_files
            self.image_files = self.template_id.image_files
            self.dashboard_html = self.template_id.template
        else:
            self.style_files = False
            self.js_files = False
            self.image_files = False
            self.dashboard_html = False

    @api.depends('style_files')
    def _compute_style_urls(self):
        """
        compute cavas urls
        """
        for rec in self:
            urls = []
            for style_file in rec.style_files:
                urls.append(style_file.url)
            rec.style_urls = urls or False

    @api.depends('js_files')
    def _compute_js_urls(self):
        """
        compute js urls
        """
        for rec in self:
            urls = []
            for js_file in rec.js_files:
                urls.append(js_file.url)
            rec.js_urls = urls or False

    @api.onchange('use_template')
    def _onchange_use_template(self):
        """
        onchange use template
        """
        if not self.use_template:
            self.template_id = False

    def export_dashboard(self):
        """
        export dashboard, use xml to describe the dashboard, and zip the files
        """
        dashboard_data = {
            'name': self.name,
            'description': self.description,

            'dashboard_html': self.dashboard_html,
            'dashboard_css': self.dashboard_css,
            'dashboard_js': self.dashboard_js,

            'use_template': self.use_template,
            'template_name': self.template_id.name if self.template_id else False,

            'style_files': self.style_files.ids,
            'js_files': self.js_files.ids,
            'image_files': self.image_files.ids,
        }

        # search configs
        any_config_infos = []
        for config in self.config_ids:
            any_config = config.export_any_config()
            any_config_infos.append(any_config)
        dashboard_data['any_config_infos'] = any_config_infos
        
        return dashboard_data

    def import_dashboard(self, dashboard_data):
        """
        import dashboard
        """
        vals = {}

        dashboard_html = dashboard_data.get('dashboard_html', '')
        config_ids = []
        any_config_info = dashboard_data.get('any_config_infos', [])
        for any_config_info in any_config_info:
            origin_config_id = any_config_info.get('id')
            if 'id' in any_config_info:
                del any_config_info['id']
            any_config_info = self.env['mana_dashboard.any_config'].import_any_config(any_config_info)
            # replace the config id in the dashboard html config_id="1"
            dashboard_html = dashboard_html.replace(
                'config_id="%s"' % origin_config_id, 'config_id="%s"' % any_config_info.id)
            config_ids.append(any_config_info.id)
        vals['config_ids'] = [(6, 0, config_ids)]

        vals['name'] = dashboard_data.get('name')
        vals['description'] = dashboard_data.get('description')

        if dashboard_data.get('template_name'):
            vals['template_id'] = self.env['mana_dashboard.dashboard_template'].search([
                ('name', '=', dashboard_data.get('template_name'))]).id

        vals['dashboard_html'] = dashboard_data.get('dashboard_html')
        vals['dashboard_css'] = dashboard_data.get('dashboard_css')
        vals['dashboard_js'] = dashboard_data.get('dashboard_js')

        vals['style_files'] = [(6, 0, dashboard_data.get('style_files'))]
        vals['js_files'] = [(6, 0, dashboard_data.get('js_files'))]
        vals['image_files'] = [(6, 0, dashboard_data.get('image_files'))]

        dashboard = self.create(vals)
        
        # create the default action and bind it to the dashboard
        val = {
            'name': 'Dashboard_' + vals['name'],
            'res_model': 'mana.dashboard',
            'params': {
                'dashboard_id': dashboard.id,
                'mode': 'view',
            },
            'tag': 'mana_dashboard',
        }
        action_id = self.env['ir.actions.client'].sudo().create(val)
        dashboard.action_id = action_id.id

        return dashboard

    def jump_to_export_url(self):
        """
        jump to export dashboard
        """
        return {
            "type": "ir.actions.act_url",
            "url": "/mana_dashboard/export_dashboard/" + str(self.id),
            "target": "new",
        }

    @api.model
    def remove_configs(self, config_infos):
        """
        remove configs
        """
        for model_name in config_infos:
            ids = config_infos[model_name]
            self.env[model_name].sudo().browse(ids).unlink()

    def write(self, vals):
        """
        override write method
        """
        if 'dashboard_html' in vals:
            config_ids = re.findall(r'config_id="(\d+)"', vals['dashboard_html'])
            if config_ids:
                old_config_ids = self.config_ids.ids
                new_config_ids = [int(config_id) for config_id in config_ids]
                remove_config_ids = list(set(old_config_ids) - set(new_config_ids))
                if remove_config_ids:
                    self.env['mana_dashboard.any_config'].sudo().browse(remove_config_ids).unlink()

        return super(ManaDashboard, self).write(vals)
    
    @api.model
    def test_button(self):
        """
        test button
        """
        return {
            "type": "ir.actions.act_url",
            "url": "https://www.openerpnext.com/",
            "target": "new",
        }
    
    def save_theme_info(self, theme_info):
        """
        save theme data
        """
        self.ensure_one()
        self.theme_info = theme_info
