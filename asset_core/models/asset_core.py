# -*- coding: utf-8 -*-
"""
@Time    : 2023/02/24 11:12
@Author  : Jason Zou
@Email   : zou.jason@qq.com
"""
from odoo import models, fields, api, _
from odoo.exceptions import UserError
import logging
import os
import time
_logger = logging.getLogger(__name__)
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

# 字段只读状态
READONLY_STATES = {
    'confirm': [('readonly', True)],
    'done': [('readonly', True)],
}
ASSET_STATUS = [
    ('normal', '正常'),
    ('alarm', '告警'),
    ('abnormal', '异常'),
    ('disconnect', '离线'),
    ('closed', '关闭')
]


class AssetCore(models.Model):
    """设备运行"""
    _name = 'asset.core'
    _description = '设备档案'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "name, id"

    name = fields.Char(string='设备', tracking=True, states=READONLY_STATES,
                       help='可填写设备序列号、设备编号、设备名称等，全局唯一')
    user_id = fields.Many2one('res.users',
                              string='负责人',
                              default=lambda self: self.env.user.id,
                              tracking=True,
                              states=READONLY_STATES,
                              help='用于选择公司内指定人员')
    job_id = fields.Many2one('staff.job',
                             string='负责人职位',
                             store=True,
                             related='user_id.staff_id.job_id')
    depart_id = fields.Many2one('staff.department',
                                string='负责人所属部门',
                                store=True,
                                related='user_id.staff_id.department_id')
    department_id = fields.Many2one('staff.department', string='设备归属部门', tracking=True, states=READONLY_STATES)
    error_detail = fields.Char(string='状态详情', states=READONLY_STATES)
    active_time = fields.Datetime(string='最近活跃时间', states=READONLY_STATES)
    installation_position = fields.Char(string='安装位置', tracking=True, states=READONLY_STATES)
    asset_tag_ids = fields.Many2many('asset.tag', string='资产标签', tracking=True, states=READONLY_STATES)
    description = fields.Text(string='内部说明', tracking=True, states=READONLY_STATES)
    image_128 = fields.Image(string="图像128", max_width=128, max_height=128, store=True,
                             tracking=True, states=READONLY_STATES)
    line_ids = fields.One2many('asset.core.line', 'bill_id', string='设备日志', states=READONLY_STATES)
    state = fields.Selection([('draft', '草稿'),
                              ('confirm', '已确认'),
                              ('closed', '已作废')], string='记录状态', default='draft', store=True, tracking=True)
    ma_roll = fields.Selection(ASSET_STATUS, string='设备状态', tracking=True, default='normal', states=READONLY_STATES)
    active = fields.Boolean(string="启用", tracking=True, default=True)
    maintenance_team_id = fields.Many2one('asset.team', string='设备管理团队')
    color = fields.Integer('Color Index')

    default_code = fields.Char(string='内部参考', help='设备内部流水号', tracking=True, states=READONLY_STATES)
    barcode = fields.Char(string='条码', copy=False, index='btree_not_null', tracking=True, states=READONLY_STATES)
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Favorite'),
    ], default='0', string="Favorite")

    @api.depends('line_ids')
    def _compute_line_ids(self):
        for line in self:
            line.entries = len(line.line_ids) + 1

    entries = fields.Integer(string='行数', compute='_compute_line_ids', )
    company_id = fields.Many2one(
        'res.company',
        string='公司',
        change_default=True,
        default=lambda self: self.env.company)

    _sql_constraints = [
        ('name_uniq', 'unique(name)', '设备序列号、设备编号、设备名称已存在'),
    ]

    task_count = fields.Integer(compute='_compute_task_count', string="维检工单")
    alarm_count = fields.Integer(compute='_compute_alarm_count', string="运行日志")

    # ----------------------------------------
    # 权限控制规则：
    # 设备负责人只管理本人的设备数据
    # 部门负责人可查看本部门所有人的设备数据
    # 平台管理员可查看所有设备的数据
    # ----------------------------------------
    @api.depends('user_id')
    def _compute_owner(self):
        """判断当前登录用户：设备负责人"""
        self.is_owner = self.env.user.has_group('asset_core.group_asset_owner')  # 设备负责人
    is_owner = fields.Boolean(string='设备负责人', readonly=True, compute='_compute_owner', )

    @api.model
    def create(self, values):
        """创建自定义设备内部流水号"""
        """创建规则：如果设备序列号为空，则用设备内部流水号自动填充设备序列号字段；如果手动输入设备序列号，则忽略填充"""
        if not values.get('default_code'):
            values['default_code'] = self.env['ir.sequence'].next_by_code('asset.core')
        result = super(AssetCore, self).create(values)
        return result

    def write(self, vals_list):
        result = super(AssetCore, self).write(vals_list)
        return result

    def unlink(self):
        for record in self:
            if record.state != 'draft':
                raise UserError('只能删除草稿状态的设备档案')
        super(AssetCore, self).unlink()

    def btn_confirm(self):
        """单据确认"""
        for line in self:
            line.write({'state': 'confirm', 'active': True})
        return

    def btn_draft(self):
        """撤销确认"""
        for line in self:
            line.write({'state': 'draft', 'active': True})
        return

    def btn_closed(self):
        """单据作废"""
        for line in self:
            line.write({'state': 'closed', 'active': False})
        return

    def action_view_task(self):
        """查我的任务"""
        return {
            'name': _('工单管理'),
            'view_mode': 'kanban,tree,form,pivot,graph,calendar',
            'domain': [('equipment_id', 'in', self.ids)],
            'res_model': 'work.sheet.management',
            'type': 'ir.actions.act_window',
            'context': {'search_default_group_status': 1, 'expand': 1},
        }

    def _compute_task_count(self):
        """查每台设备档案在处理工单统计数据"""
        task_data = self.env['work.sheet.management']._read_group([
            ('equipment_id', 'in', self.ids)], ['equipment_id'], ['equipment_id'])
        result = dict((data['equipment_id'][0], data['equipment_id_count']) for data in task_data)
        for task in self:
            if not len(result):
                task.task_count = 0
                continue
            task.task_count = result.get(task.id, 0)

    def action_view_alarm(self):
        """查设备告警日志"""
        return {
            'name': _('日志管理'),
            'view_mode': 'tree,graph,pivot,calendar',
            'domain': [('bill_id', 'in', self.ids)],
            'res_model': 'asset.core.line',
            'type': 'ir.actions.act_window',
        }

    def _compute_alarm_count(self):
        """查每台设备设备告警日志统计数据"""
        task_data = self.env['asset.core.line']._read_group([
            ('bill_id', 'in', self.ids)], ['bill_id'], ['bill_id'])
        result = dict((data['bill_id'][0], data['bill_id_count']) for data in task_data)
        for task in self:
            if not len(result):
                task.alarm_count = 0
                continue
            task.alarm_count = result.get(task.id, 0)


class AssetCoreLine(models.Model):
    """设备运行日志"""
    _name = 'asset.core.line'
    _inherits = {'task': 'task_id'}
    _description = '设备运行日志'

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

    @api.model
    def _default_sequence(self):
        return self._context.get('entries', 1)

    sequence = fields.Integer(string='行号', required=True, default=lambda self: self._context.get('entries', 1), )
    alarm_time = fields.Datetime(string='日期/时间')
    path_route = fields.Char(string='路径')
    measure_point = fields.Char(string='测点')
    head_line = fields.Char(string='标题')
    numerical_value = fields.Char(string='数值')
    percentage = fields.Char(string='百分比')
    ma_roll = fields.Selection(ASSET_STATUS, string='设备状态')
    error_detail = fields.Char(string='状态详情')
    verification_date = fields.Datetime(string='确认日期')
    confirmed_description = fields.Char(string='确认说明')
    confirmed_by = fields.Many2one('res.users', string='确认人', help='确认人')
    active = fields.Boolean(string="启用", default=True)
    send = fields.Boolean(string="已邮件告警", default=False)
    bill_id = fields.Many2one('asset.core', string="设备档案", ondelete='cascade', help='关联主表')

    def btn_ok_batch(self):
        """确认设备运行日志状态"""
        for line in self:
            line.write({
                'verification_date': fields.Datetime.now(),
                'confirmed_description': '已确认',
                'confirmed_by': self.env.user.id,
                'active': False
            })
        return

    def alarm_scheduler(self):
        """确认设备运行日志状态"""
        alarm_scheduler_ids = \
            self.with_user(2).env['asset.core.line'].search([
                ('send', '=', False), ('ma_roll', 'not in', ['normal', 'closed'])])
        if len(alarm_scheduler_ids) == 0:
            return
        for line in alarm_scheduler_ids:
            # 创建邮件正文
            roll_status = ''
            if line['ma_roll'] == 'alarm':
                roll_status = '告警'
            if line['ma_roll'] == 'abnormal':
                roll_status = '异常'
            if line['ma_roll'] == 'disconnect':
                roll_status = '离线'

            msg_body = self.create_mail_contextbg(
                line['alarm_time'], line['path_route'], line['measure_point'], line['head_line'],
                line['numerical_value'], line['percentage'], roll_status, line['error_detail'])
            self.env['mail.mail'].create({
                'auto_delete': False,
                'to_delete': True,
                'state': 'outgoing',
                'mail_server_id': self.env['ir.mail_server'].search([('name', '=', '发件服务器')]).id,
                'record_name': time.strftime('%Y-%m-%d %H-%M-%S'),
                'message_type': 'email',
                'reply_to': 'zou.jason@qq.com',
                'email_from': 'it-support@dingyang.com',
                'email_cc': 'zou.jason@qq.com',
                'email_to': 'zou.jason@qq.com',
                'subject': '设备运行异常告警！{}::{}::{}'.format(line['name'], roll_status, line['error_detail']),
                'body_html': msg_body,
            }).send()
            line.write({'send': True})   # 修改已成功告警的设备运行日志记录为“已邮件告警”状态
        return

    def create_mail_contextbg(self, line_00, line_01, line_02, line_03,
                              line_04, line_05, line_06, line_07):
        # 输出邮件页面内容
        msg_body = """
        <table align="center" border="1" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;">
        <tr bgcolor="#cccccc">
        <th width="10%" align = "center"><font size="2" color="#0000FF">日期/时间</font></th>
        <th width="10%" align = "center"><font size="2" color="#0000FF">路径</font></th>
        <th width="10%" align = "center"><font size="2" color="#0000FF">测点</font></th> 
        <th width="10%" align = "center"><font size="2" color="#0000FF">标题</font></th> 
        <th width="10%" align = "center"><font size="2" color="#0000FF">数值</font></th> 
        <th width="10%" align = "center"><font size="2" color="#0000FF">百分比</font></th> 
        <th width="10%" align = "center"><font size="2" color="#0000FF">设备状态</font></th> 
        <th width="10%" align = "center"><font size="2" color="#0000FF">状态详情</font></th>
        </tr>"""
        tr = """
        <tr>
        <td align = "center"><font size="2">{}</font></td>
        <td  align = "center"><font size="2">{}</font></td> 
        <td  align = "center"><font size="2">{}</font></td> 
        <td  align = "center"><font size="2">{}</font></td> 
        <td  align = "center"><font size="2">{}</font></td>  
        <td  align = "center"><font size="2">{}</font></td>  
        <td  align = "center"><font size="2">{}</font></td>  
        <td  align = "center"><font size="2">{}</font></td>  
        </tr>
        </table>""".format(line_00 or '', line_01 or '', line_02 or '', line_03 or '',
                           line_04 or '', line_05 or '', line_06 or '', line_07 or '')
        msg_body += tr
        body = msg_body + u'<br/>'
        return body


class AssetTeam(models.Model):
    _name = 'asset.team'
    _description = '设备管理团队'

    name = fields.Char('团队名称', required=True, translate=True)
    code = fields.Char()
    active = fields.Boolean(string="启用", default=True)
    company_id = fields.Many2one(
        'res.company',
        string='公司',
        change_default=True,
        default=lambda self: self.env.company)
    member_ids = fields.Many2many('res.users', 'asset_team_users_rel', string="团队成员")
    color = fields.Integer("Color Index", default=0)
    equipment_ids = fields.One2many('asset.core', 'maintenance_team_id', copy=False)

    # 仅用于仪表板
    todo_request_count = fields.One2many('asset.core', string="相关设备台套", copy=False, compute='_compute_todo_requests')
    todo_asset_count = fields.Integer(string="设备台套计数", compute='_compute_todo_requests')
    todo_count_normal = fields.Integer(string="正常设备", compute='_compute_todo_requests')
    todo_count_alarm = fields.Integer(string="告警设备", compute='_compute_todo_requests')
    todo_count_abnormal = fields.Integer(string="异常设备", compute='_compute_todo_requests')
    todo_count_disconnect = fields.Integer(string="离线设备", compute='_compute_todo_requests')
    todo_count_closed = fields.Integer(string="关闭设备", compute='_compute_todo_requests')

    def _compute_todo_requests(self):
        """统计每个设备管理团队下的设备"""
        for team in self:
            team.todo_request_count = self.env['asset.core'].search([('maintenance_team_id', '=', team.id)])
            team.todo_asset_count = len(team.todo_request_count)

            team.todo_count_normal = self.env['asset.core'].search_count(
                [('maintenance_team_id', '=', team.id), ('ma_roll', '=', 'normal')])
            team.todo_count_alarm = self.env['asset.core'].search_count(
                [('maintenance_team_id', '=', team.id), ('ma_roll', '=', 'alarm')])
            team.todo_count_abnormal = self.env['asset.core'].search_count(
                [('maintenance_team_id', '=', team.id), ('ma_roll', '=', 'abnormal')])
            team.todo_count_disconnect = self.env['asset.core'].search_count(
                [('maintenance_team_id', '=', team.id), ('ma_roll', '=', 'disconnect')])
            team.todo_count_closed = self.env['asset.core'].search_count(
                [('maintenance_team_id', '=', team.id), ('ma_roll', '=', 'closed')])

    def action_asset_team_field(self):
        """查看设备管理清单"""
        return {
            'name': _('设备档案'),
            'view_mode': 'kanban,tree,form,pivot,graph,calendar',
            'res_model': 'asset.core',
            'domain': [('maintenance_team_id', '=', self.id)],
            'type': 'ir.actions.act_window',
        }

    def action_asset_core_line_field(self):
        """查看日志管理"""
        team_ids = []
        for i in self.equipment_ids:
            team_ids.append(i.id)
        return {
            'name': _('日志管理'),
            'view_mode': 'tree,graph,pivot,calendar',
            'res_model': 'asset.core.line',
            'domain': [('bill_id', 'in', team_ids)],
            'type': 'ir.actions.act_window',
        }

    def action_work_sheet_management_field(self):
        """查看工单管理"""
        team_ids = []
        for i in self.equipment_ids:
            team_ids.append(i.id)
        return {
            'name': _('工单管理'),
            'view_mode': 'kanban,tree,form,pivot,graph,calendar',
            'res_model': 'work.sheet.management',
            'domain': [('equipment_id', 'in', team_ids)],
            'type': 'ir.actions.act_window',
        }

    @api.depends('equipment_ids')
    def _compute_equipment(self):
        for team in self:
            team.equipment_count = len(team.equipment_ids)


class Timeline(models.Model):
    _inherit = 'timeline'

    @api.model
    def create(self, vals):
        """创建工作记录时，更新对应task的status等字段"""
        res = super(Timeline, self).create(vals)
        set_status = vals.get('set_status')
        task_id = vals.get('task_id')
        just_done = vals.get('just_done')
        task = self.with_user(2).env['asset.core.line'].search([('task_id', '=', task_id)])
        task_status = self.with_user(2).env['task.status'].search([('state', '=', 'done')])
        active = True
        if set_status or just_done:
            if task_status.id == set_status:
                active = False
            task.write({'status': set_status,
                        'confirmed_description': just_done,
                        'verification_date': fields.Datetime.now(),
                        'confirmed_by': self.env.user.id,
                        'active': active
                        })
        return res
