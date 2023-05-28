# -*- coding: utf-8 -*-
"""
@Time    : 2022/12/26 21:40
@Author  : Jason Zou
@Email   : zou.jason@qq.com
"""
from odoo import models, fields, exceptions, api, _
import os
import json
import logging
import requests
_logger = logging.getLogger(__name__)
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
headers = {'content-type': 'application/json'}


class WxApproval(models.Model):
    _name = 'wx.approval'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = '审批配置'

    name = fields.Char(string='审批名称')
    model_id = fields.Many2one('ir.model', ondelete='cascade', string='审批模型')
    is_external_tpl = fields.Boolean(string='外部内容模板', default=True)
    template_id = fields.Char(string='审批流模板ID', help='可在审批模板的模板编辑页面浏览器Url链接中获得')
    submit_actions_server_id = fields.Many2one('ir.actions.server', ondelete='cascade', string='提交审批执行动作')
    accept_actions_server_id = fields.Many2one('ir.actions.server', ondelete='cascade', string='通过执行动作')
    reject_actions_server_id = fields.Many2one('ir.actions.server', ondelete='cascade', string='驳回执行动作')
    cancel_actions_server_id = fields.Many2one('ir.actions.server', ondelete='cascade', string='取消时执行动作')
    enable = fields.Boolean(string='启用', default=False)
    show_link = fields.Char(string='show_link')

    template_fields = fields.One2many('wx.approval.template_fields', 'bill_id', string='对接配置字段')

    _sql_constraints = [
        ('name_uniq', 'unique(name)', '已存在相同“审批名称”了，请设置另一个。'),
    ]

    def subscribe(self):
        """启用配置"""
        act_record = self.with_user(2).env['ir.actions.server']
        commit_record = act_record.search([
            ('name', '=', '提交' + self.name + '审批'),
            ('model_name', '=', self.model_id.model)
        ])
        search_record = act_record.search([
            ('name', '=', '查看' + self.name + '审批'),
            ('model_name', '=', self.model_id.model)
        ])
        for pd in self:
            pd.write({'enable': True})
            if len(commit_record) and len(search_record):
                act_record.write({
                    'name': '提交' + self.name + '审批',
                    'model_id': self.model_id.id,
                    'binding_model_id': self.model_id.id,
                    'code': 'action = records.submit_to_wechat()',
                    'model_name': self.model_id.model,
                })
                act_record.write({
                    'name': '查看' + self.name + '审批',
                    'model_id': self.model_id.id,
                    'binding_model_id': self.model_id.id,
                    'code': "action = env['wx.approval.obj'].object_approval_status()",
                    'model_name': self.model_id.model,
                })
            else:
                act_record.create({
                    'name': '提交' + self.name + '审批',
                    'state': 'code',
                    'binding_type': 'action',
                    'binding_view_types': 'list,form',
                    'model_id': self.model_id.id,
                    'binding_model_id': self.model_id.id,
                    'code': 'action = records.submit_to_wechat()',
                    'type': 'ir.actions.server',
                    'usage': 'ir_actions_server',
                    'model_name': self.model_id.model,
                })
                act_record.create({
                    'name': '查看' + self.name + '审批',
                    'state': 'code',
                    'binding_type': 'action',
                    'binding_view_types': 'list,form',
                    'model_id': self.model_id.id,
                    'binding_model_id': self.model_id.id,
                    'code': "action = env['wx.approval.obj'].object_approval_status()",
                    'type': 'ir.actions.server',
                    'usage': 'ir_actions_server',
                    'model_name': self.model_id.model,
                })
        return

    def unsubscribe(self):
        """禁用配置"""
        ir_action = self.with_user(2).env['ir.actions.actions']
        act_record = self.with_user(2).env['ir.actions.server']
        commit_record = act_record.search([
            ('name', '=', '提交' + self.name + '审批'),
            ('model_name', '=', self.model_id.model)
        ])
        search_record = act_record.search([
            ('name', '=', '查看' + self.name + '审批'),
            ('model_name', '=', self.model_id.model)
        ])
        for pd in self:
            pd.write({'enable': False})
            if len(commit_record) and len(search_record):
                act_record.search([
                    ('name', '=', '提交' + self.name + '审批'),
                    ('model_name', '=', 'model_record.model')
                ]).unlink()
                act_record.search([
                    ('name', '=', '查看' + self.name + '审批'),
                    ('model_name', '=', 'model_record.model')
                ]).unlink()
                ir_action.search([
                    ('binding_model_id', '=', self.model_id.id),
                    ('id', '=', commit_record.id)
                ]).unlink()
                ir_action.search([
                    ('binding_model_id', '=', self.model_id.id),
                    ('id', '=', search_record.id)
                ]).unlink()
        return

    def gen_access_token(self):
        """授权信息，获取企微Access Token"""
        record = self.env['res.company'].search([('id', '=', '1')])
        token_args = {
            "corpid": record['corp_id'],  # 企业id
            "corpsecret": record['corp_secret'],  # 企业Secret
        }
        try:
            ret = requests.get(record['token_url'].format(record['corp_id'], record['corp_secret']),
                               json=token_args, headers=headers)
        except Exception as e:
            _logger.error("获取企微Access Token时，连接失败。The exception: " + str(e))
            return
        if ret.status_code == 200:
            text = json.loads(ret.text)
            token = text["access_token"]
            return token

    def interface_get_approval_template(self, token, template_id):
        gen_template_url = self.with_user(2).env['ewi.interface'].search([('name', '=', '获取审批模板详情')]).url
        template_args = {
            "template_id": template_id
        }
        try:
            ret = requests.post(gen_template_url.format(token), json=template_args, headers=headers)
        except Exception as e:
            _logger.error('企业微信获取模板信息时连接失败：' + str(e))
            return
        if ret.status_code == 200:
            text = json.loads(ret.text)
            errcode = text['errcode']
            if errcode == 0:
                return text
            else:
                errmsg = text['errmsg']
                _logger.error('企业微信获取模板信息失败，errcode:"' + str(errcode) + '", errmsg:"' + errmsg + '" !')
                if str(errcode) == '42001':
                    _logger.error('企业微信接口“access_token已过期，需要重新获取一次”。')
                return
        else:
            _logger.error('企业微信获取模板信息时连接失败，连接状态:"' + str(ret.status_code) + '"')
            return

    def sync_external_tpl(self):
        """同步外部内容模板"""
        eop_record = self.with_user(2).env['res.company'].search([('id', '=', '1')]).access_token
        etc_model = self.with_user(2).env['wx.approval.template_fields']
        if len(eop_record) != 0:
            token = eop_record
        else:
            token = self.gen_access_token()
        """从企业微信模板URL中获得"""
        text = self.interface_get_approval_template(token, self.template_id)
        if not text:
            raise exceptions.Warning('获取企业微信审批模板失败，详情请查询后台日志。')
        errcode = text['errcode']
        if errcode == 0:
            template_names = text['template_names']
            template_names_text = ''
            for template_name in template_names:
                template_names_lang = template_name['lang']
                if template_names_lang == 'zh_CN':
                    template_names_text = template_name['text']
            template_content = text['template_content']
            controls = template_content['controls']
            for control in controls:
                control_property = control['property']
                control_type = control_property['control']
                control_id = control_property['id']
                titles = control_property['title']
                title_name = ''
                for title in titles:
                    title_lang = title['lang']
                    if title_lang == 'zh_CN':
                        title_name = title['text']
                placeholders = control_property['placeholder']
                placeholder_name = ''
                for placeholder in placeholders:
                    placeholder_lang = placeholder['lang']
                    if placeholder_lang == 'zh_CN':
                        placeholder_name = placeholder['text']
                require = control_property['require']
                if require == 1:
                    require = True
                else:
                    require = False
                if 'config' in control:
                    config = control['config']
                else:
                    config = False
                if config and 'table' in config:
                    children = config['table']['children']
                    for child in children:
                        child_property = child['property']
                        child_type = child_property['control']
                        child_id = child_property['id']
                        child_titles = child_property['title']
                        child_title_name = ''
                        for child_title in child_titles:
                            child_title_lang = child_title['lang']
                            if child_title_lang == 'zh_CN':
                                child_title_name = child_title['text']
                        child_placeholders = child_property['placeholder']
                        child_placeholder_name = ''
                        for child_placeholder in child_placeholders:
                            child_placeholder_lang = child_placeholder['lang']
                            if child_placeholder_lang == 'zh_CN':
                                child_placeholder_name = child_placeholder['text']
                        child_require = child_property['require']
                        if child_require == 1:
                            child_require = True
                        else:
                            child_require = False
                        if 'config' in child:
                            child_config = child['config']
                        else:
                            child_config = False
                        etc_record = etc_model.search([('ext_id', '=', child_id),
                                                       ('is_in_table', '=', True),
                                                       ('template_id', '=', self.template_id),
                                                       ('bill_id', '=', self.id)])
                        if etc_record:
                            etc_record.write({
                                'template_name': template_names_text,
                                'control': child_type,
                                'field': child_title_name,
                                'placeholder': child_placeholder_name,
                                'require': child_require,
                                'is_in_table': True,
                                'model_id': self.model_id.id,
                            })
                        else:
                            etc_model.create({
                                'bill_id': self.id,
                                'template_id': self.template_id,
                                'template_name': template_names_text,
                                'ext_id': child_id,
                                'control': child_type,
                                'field': child_title_name,
                                'placeholder': child_placeholder_name,
                                'require': child_require,
                                'is_in_table': True,
                                'model_id': self.model_id.id,
                            })
                else:
                    etc_record = etc_model.search([('ext_id', '=', control_id),
                                                   ('is_in_table', '=', False),
                                                   ('template_id', '=', self.template_id),
                                                   ('bill_id', '=', self.id)
                                                   ])
                    if etc_record:
                        etc_record.write({
                            'template_name': template_names_text,
                            'control': control_type,
                            'field': title_name,
                            'placeholder': placeholder_name,
                            'require': require,
                            'is_in_table': False,
                            'model_id': self.model_id.id,
                        })
                    else:
                        etc_model.create({
                            'bill_id': self.id,
                            'template_id': self.template_id,
                            'template_name': template_names_text,
                            'ext_id': control_id,
                            'control': control_type,
                            'field': title_name,
                            'placeholder': placeholder_name,
                            'require': require,
                            'is_in_table': False,
                            'model_id': self.model_id.id,
                        })


class WxApprovalTemplateFields(models.Model):
    _name = 'wx.approval.template_fields'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = '审批模板字段'

    bill_id = fields.Many2one('wx.approval', string="审批配置", ondelete='cascade', help='关联主表')
    # 企业微信字段
    template_id = fields.Char('企微审批模板id', help='企业微信请求返回字段')
    template_name = fields.Char(string='模板名称', help='企业微信请求返回字段')
    field = fields.Char(string='控件名称', help='企业微信请求返回字段')
    control = fields.Char(string='控件类型', help='企业微信请求返回字段')
    placeholder = fields.Char(string='控件说明', help='企业微信请求返回字段')
    require = fields.Char(string='是否必填', help='企业微信请求返回字段')
    ext_id = fields.Char(string='控件ID', help='企业微信请求返回字段')
    is_in_table = fields.Boolean(string='是否表单内控件', help='企业微信请求返回字段')
    sequence = fields.Integer(string='序号')

    # ODOO对象字段
    field_id = fields.Many2one('ir.model.fields',
                               ondelete='cascade',
                               domain="[('model_id', '=', model_id)]",   # 过滤数据，相当于where条件
                               string='模型字段OD',
                               help='odoo本地模型字段')
    model_id = fields.Integer(string='审批模型ID')
    field_name = fields.Char(string='字段名称OD',
                             related='field_id.name',
                             readonly=True,
                             store=True,
                             help='odoo本地模型字段')
    field_model = fields.Char(string='模型名称OD',
                              related='field_id.model',
                              readonly=True,
                              store=True,
                              help='odoo本地模型字段')


