# -*- coding: utf-8 -*-
"""
@Time    : 2022/12/26 21:40
@Author  : Jason Zou
@Email   : zou.jason@qq.com
"""
from odoo import models, fields, _


class WxApprovalRecord(models.Model):
    _name = 'wx.approval.record'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = '详细审批记录'

    approval_obj_id = fields.Char(string='所属审批单')
    apply_user_name = fields.Char(string='提交人')
    user_name = fields.Char(string='审批人')
    item_status = fields.Char(string='审批操作')
    speech = fields.Char(string='审批意见')
    step = fields.Char(string='节点')
    detail_link = fields.Char(string='操作')

    def user_record(self, record_id):
        if record_id == 1:
            return {
                'name': _('我的已办'),
                'view_mode': 'tree',
                # 'domain': [('approval_obj_id', 'in', self.ids), ('user_name', '=', self.env.uid)],
                'res_model': 'wx.approval.record_ids',
                'type': 'ir.actions.act_window',
                'target': 'current',
            }
        elif record_id == 2:
            return {
                'name': _('我的待办'),
                'view_mode': 'tree',
                # 'domain': [('approval_obj_id', 'in', self.ids), ('user_name', '=', self.env.uid)],
                'res_model': 'wx.approval.record_ids',
                'type': 'ir.actions.act_window',
                'target': 'current',
            }
