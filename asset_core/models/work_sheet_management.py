# -*- coding: utf-8 -*-
"""
@Time    : 2023/02/26 16:08
@Author  : Jason Zou
@Email   : zou.jason@qq.com
"""
from odoo import models, fields, api, _
import logging
import os
_logger = logging.getLogger(__name__)
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
ASSET_STATUS = [
    ('normal', '正常'),
    ('alarm', '告警'),
    ('abnormal', '异常'),
    ('disconnect', '离线'),
    ('closed', '关闭')
]


class WorkSheetManagement(models.Model):
    """设备工单"""
    _name = 'work.sheet.management'
    _description = '设备工单'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _inherits = {'task': 'task_id'}

    @api.model
    def _read_group_status_ids(self, status, domain, order):
        """看板或列表视图上分组时显示所有阶段（即使该阶段没有记录）"""
        status_ids = self.env['task.status'].search([])
        return status_ids

    @api.model
    def _default_status(self):
        """创建工单时，阶段默认为todo状态的阶段，即 新建"""
        return self.task_id._default_status()

    task_id = fields.Many2one('task',
                              string='任务',
                              ondelete='cascade',
                              required=True)
    status = fields.Many2one(
        'task.status',
        string='阶段状态',
        group_expand='_read_group_status_ids',
        default=_default_status,
        tracking=True,
        ondelete='restrict',
        domain="[('project_type_id', '=', False)]",
    )

    asset_task_type = fields.Many2one('asset.task.type', string='工单类', help='派工单任务分类')
    active_time = fields.Datetime(string='最近活跃时间')
    job_id = fields.Many2one('staff.job',
                             string='负责人职位',
                             store=True,
                             related='user_id.staff_id.job_id')
    depart_id = fields.Many2one('staff.department',
                                string='负责人所属部门',
                                store=True,
                                related='user_id.staff_id.department_id')
    department_id = fields.Many2one('staff.department', string='设备归属部门', tracking=True)
    error_detail = fields.Char(string='状态详情', tracking=True)
    installation_position = fields.Char(string='安装位置', tracking=True)
    description = fields.Text(string='处理结果', tracking=True)
    ma_roll = fields.Selection(ASSET_STATUS, string='设备状态', tracking=True)
    active = fields.Boolean(string='待归档', default=True, tracking=True)
    image_128 = fields.Image(string="图像128", max_width=128, max_height=128, store=True, tracking=True)
    color = fields.Integer(string='color')
    company_id = fields.Many2one(
        'res.company',
        string='公司',
        change_default=True,
        default=lambda self: self.env.company)

    equipment_id = fields.Many2one('asset.core', '设备')

    @api.depends('user_id')
    def _compute_user_admin(self):
        """判断当前登录用户：系统管理员可修改权限"""
        self.is_manager = self.env.user.has_group('base.user_admin')  # 系统管理员可修改权限

    is_manager = fields.Boolean(string='系统管理员', readonly=True, compute='_compute_user_admin', )


class Timeline(models.Model):
    _inherit = 'timeline'

    @api.model
    def create(self, vals):
        """创建工作记录时，更新对应task的status等字段"""
        res = super(Timeline, self).create(vals)
        set_status = vals.get('set_status')
        task_id = vals.get('task_id')
        just_done = vals.get('just_done')
        task = self.with_user(2).env['work.sheet.management'].search([('task_id', '=', task_id)])
        task_status = self.with_user(2).env['task.status'].search([('state', '=', 'done')])
        active = True
        if set_status or just_done:
            if task_status.id == set_status:
                active = False
            task.write({'status': set_status,
                        'description': just_done,
                        'write_date': fields.Datetime.now(),
                        'write_uid': self.env.user.id,
                        'active': active
                        })
        return res
