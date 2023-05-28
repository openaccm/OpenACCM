# -*- coding: utf-8 -*-
"""
@Time    : 2023/02/13 14:43
@Author  : Jason Zou
@Email   : zou.jason@qq.com
"""
from odoo import models, fields, api
# unplanned, 非计划维修
# preventive, 预防性维护


class WorkSheetWizard(models.TransientModel):
    _name = 'work.sheet.wizard'
    _description = '根据设备档案生成工单向导'

    asset_task_type = fields.Many2one('asset.task.type', string='工单类', required=True)
    owner = fields.Many2one('res.users', string='负责人', required=True, ondelete='cascade',
                            help='用于选择公司内指定人员')

    def btn_new_task(self):
        """新建任务分派工单"""
        model = self.env.context.get('active_model')
        active_ids = self.env.context.get('active_ids')
        line_ids = self.env[model].browse(active_ids)
        for line_id in line_ids:
            self.env['work.sheet.management'].create(
                {
                    'asset_task_type': self.asset_task_type.id,
                    'name': line_id.name,
                    'user_id': self.owner.id,
                    'department_id': line_id.department_id.id,
                    'error_detail': line_id.error_detail,
                    'installation_position': line_id.installation_position,
                    'image_128': line_id.image_128,
                    'active_time': line_id.active_time,
                    'ma_roll': line_id.ma_roll,
                    'active': True,
                    'equipment_id': line_id.id
                })

