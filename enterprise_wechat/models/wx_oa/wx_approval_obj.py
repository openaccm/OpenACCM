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
import datetime
_logger = logging.getLogger(__name__)
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
headers = {'content-type': 'application/json'}
Approval_state = [
    ('0', '待提交'),
    ('1', '审批中'),
    ('2', '已通过'),
    ('3', '已驳回'),
    ('4', '已撤销'),
    ('6', '通过后撤销'),
    ('7', '已删除'),
    ('10', '已支付')
]


def _compute_state(sp_state):
    """计算申请单状态"""
    # 审批状态：1 - 审批中；2 - 已同意；3 - 已驳回；4 - 已转审；11 - 已退回；12 - 已加签；13 - 已同意并加签
    value = ''
    if sp_state == 0:
        value = '待提交'
    elif sp_state == 1:
        value = '审批中'
    elif sp_state == 2:
        value = '已同意'
    elif sp_state == 3:
        value = '已驳回'
    elif sp_state == 4:
        value = '已转审'
    elif sp_state == 11:
        value = '已退回'
    elif sp_state == 12:
        value = '已加签'
    elif sp_state == 13:
        value = '已同意并加签'
    return value


class WxApprovalObj(models.Model):
    _name = 'wx.approval.obj'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = '审批单据'

    @api.model
    def _select_objects(self):
        records = self.with_user(2).env['wx.approval'].search([])
        models = self.with_user(2).env['ir.model'].search(
            [('id', 'in', [int(record.model_id) for record in records])])
        return [(model.model, model.name) for model in models]

    res_name = fields.Char(string='单据记录名称')
    res = fields.Reference(string='相关记录', selection='_select_objects')
    approval_id = fields.Many2one('wx.approval', string='所属审批', ondelete='cascade')
    approval_state = fields.Selection(Approval_state, string='当前审批状态')
    submit_user_id = fields.Many2one('res.users', string='提交人', ondelete='cascade')
    submit_time = fields.Datetime(string='提审时间')
    sp_no = fields.Char(string='审批编号')
    record_ids = fields.One2many('wx.approval.record_ids',
                                 'bill_id',
                                 ondelete='cascade',
                                 readonly=True,
                                 string='审批记录')

    def name_get(self):
        res = []
        for line in self:
            res.append((line.id, str(line.res_name) + ' ' + str(line.submit_user_id.name)))
        return res

    def unlink(self):
        for mia in self:
            if mia.approval_status != '待提交':
                raise exceptions.Warning('该申请已提交企业微信审批，不可删除！')
        return super(WxApprovalObj, self).unlink()

    def get_local_time(self):
        # 将utc时间转化为本地时间
        time_now = (datetime.datetime.utcnow() + datetime.timedelta(hours=8))
        time_text = time_now.strftime("%Y-%m-%d %H:%M:%S")
        return time_text

    def gen_approval_access_token(self):
        """授权信息，获取“审批应用”Access Token"""
        record = self.env['res.company'].search([('id', '=', '1')])
        token_args = {
            "corpid": record['corp_id'],  # 企业id
            "corpsecret": record['sp_Secret'],  # 审批应用Secret
        }
        try:
            ret = requests.get(record['token_url'].format(record['corp_id'], record['sp_Secret']),
                               json=token_args, headers=headers)
        except Exception as e:
            _logger.error("获取审批应用Access Token时，连接失败。The exception: " + str(e))
            return
        if ret.status_code == 200:
            text = json.loads(ret.text)
            token = text["access_token"]
            return token

    def submit_to_wechat(self):
        """提交审批"""
        eop_record = self.with_user(2).env['res.company'].search([('id', '=', '1')]).sp_access_token
        submit_approval_url = self.with_user(2).env['ewi.interface'].search([('name', '=', '提交审批申请')]).url
        he_model = self.with_user(2).env['staff']
        if len(eop_record) != 0:
            token = eop_record
        else:
            token = self.gen_approval_access_token()
        for mia in self:
            if mia.approval_state == '0':
                create_user_record = he_model.search([('user_id', '=', 149)])   # 测试数据
                # create_user_record = he_model.search([('user_id', '=', self.submit_user_id.id)])    # 申请人企微id
                cu_id = create_user_record[0].work_no
                data = {
                    # 审批人模式：
                    # 0-通过接口指定审批人、抄送人（此时approver、notifyer等参数可用）;
                    # 1-使用此模板在管理后台设置的审批流程(需要保证审批流程中没有“申请人自选”节点)，支持条件审批。默认为0
                    'creator_userid': cu_id,
                    'template_id': mia.approval_id.template_id,
                    'use_template_approver': 1,
                    'apply_data': {
                        'contents': [
                            # 部门
                            # {
                            #     'control': 'Contact',
                            #     'id': 'Contact-1571757958847',
                            #     'value': {
                            #         'value': {
                            #             'text': '计划部',
                            #         },
                            #     }
                            # },
                            # 姓名
                            {
                                'control': 'Text',
                                'id': 'Text-1610333854036',
                                'value': {
                                    'text': '王乐乐'
                                }
                            },
                            # 别名
                            # {
                            #     'control': 'Text',
                            #     'id': 'Text-1571757840595',
                            #     'value': {
                            #         'text': '210901888',
                            #     }
                            # },
                            # 职务
                            # {
                            #     'control': 'Text',
                            #     'id': 'Text-1571758080613',
                            #     'value': {
                            #         'text': '计划管理',
                            #     }
                            # },
                            # 帐号
                            # {
                            #     'control': 'Text',
                            #     'id': 'Text-1571757847906',
                            #     'value': {
                            #         'text': '210901888',
                            #     }
                            # },
                            # 手机
                            # {
                            #     'control': 'Number',
                            #     'id': 'Number-1571757935279',
                            #     'value': {
                            #         'new_number': '13900009876',
                            #     }
                            # },
                            # 邮箱
                            # {
                            #     'control': 'Text',
                            #     'id': 'Text-1571757952538',
                            #     'value': {
                            #         'text': 'wanglele@dingyang.com',
                            #     }
                            # }
                        ]
                    },
                    "summary_list": [
                        {
                            "summary_info": [{
                                "text": '主题: ' + str(self.res_name) + '审批',
                                "lang": "zh_CN",
                            }]
                        },
                        {
                            "summary_info": [{
                                "text": '时间: ' + str(self.get_local_time()),
                                "lang": "zh_CN",
                            }]
                        }
                    ]
                }
                ret = requests.post(submit_approval_url.format(token), json=data, headers=headers)
                if ret.status_code == 200:
                    text = json.loads(ret.text)
                    try:
                        errcode = text['errcode']
                        if errcode == 0:
                            approval_state = '1'    # 审批中
                            mia.approval_state = approval_state
                            submit_time = self.get_local_time()     # 提审时间
                            mia.submit_time = submit_time
                            mia.sp_no = text["sp_no"]
                            self.multi_get_approval_status()   # 返回企业微信审批记录
                        else:
                            errmsg = text['errmsg']
                            _logger.error('0.获取企微返回信息异常，异常原因 + "' + str(errmsg) + '"')
                            mia.sp_no = "提交失败%s" % errmsg
                    except Exception as e:
                        _logger.error('1.获取企微返回信息异常，异常原因 + "' + str(e) + '"')
                        mia.sp_no = "提交失败%s, %s" % (str(e), text)
                else:
                    _logger.error('连接企微失败，连接错误代码:' + str(ret.status_code))
                    raise exceptions.Warning('连接企微失败，连接错误代码:' + str(ret.status_code) + '，详情请查看后台日志')

    def cancel_to_wechat(self):
        """撤销审批"""
        for pd in self:
            # 设置ODOO系统页面值
            pd.write({'approval_state': '0', 'submit_time': False, 'sp_no': False, 'record_ids': False})
        """调用接口撤销企业微信在审批的对应单据"""
        return

    def gen_sp_userid(self, userid):
        """查审批流程名"""
        user_id = self.with_user(2).env['staff'].search([('work_no', '=', userid)])
        if len(user_id):
            user_name = user_id.name + '({})'.format(userid)
        else:
            user_name = '管理员'
        return user_name

    def multi_get_approval_status(self):
        """
        单记录，详细审批记录
        申请单状态：0-待提交；1-审批中；2-已通过；3-已驳回；4-已撤销；6-通过后撤销；7-已删除；10-已支付
        """
        token = self.gen_approval_access_token()
        for mia in self:
            if mia.approval_state == '1':
                mia.get_approval_status(token)

    def auto_get_approval_status(self):
        """
        多记录，详细审批记录
        申请单状态：0-待提交；1-审批中；2-已通过；3-已驳回；4-已撤销；6-通过后撤销；7-已删除；10-已支付
        """
        token = self.gen_approval_access_token()
        mia_list = self.with_user(2).search([('active', '=', True),
                                             ('approval_state', '=', '1'),
                                             ('sp_no', '!=', None)
                                             ])
        for mia in mia_list:
            mia.get_approval_status(token)

    def get_approval_status(self, token):
        """
        申请单状态：0-待提交；1-审批中；2-已通过；3-已驳回；4-已撤销；6-通过后撤销；7-已删除；10-已支付
        """
        record_obj = self.with_user(2).env['wx.approval.record_ids']
        record_ids = record_obj.search([('bill_id', '=', self.id)])
        approval_url = self.with_user(2).env['ewi.interface'].search([('name', '=', '获取审批申请详情')]).url
        approval_url_full = approval_url.format(token)
        approval_args = {
            'sp_no': self.sp_no
        }
        try:
            ret = requests.post(approval_url_full, json=approval_args, headers=headers)
            if ret.status_code == 200:
                text = json.loads(ret.text)
                errcode = text['errcode']
                if errcode == 0:
                    info = text['info']
                    sp_status = info['sp_status']
                    self.approval_state = '{}'.format(sp_status)     # 申请单状态
                    if len(record_ids):
                        record_ids.unlink()
                    applicant = info['applyer']['userid']  # 申请人信息
                    dl = {
                        'bill_id': self.id,
                        'sequence': 1,
                        'step': self.gen_sp_userid(applicant),
                        'item_status': '提交',
                        'sp_time': self.submit_time
                    }
                    record_obj.create(dl)
                    contents = info['sp_record']  # 审批流程信息
                    i = 2
                    for content in contents:
                        sp_status = content['sp_status']
                        sp_userid = content['details'][0]['approver']['userid']
                        sp_speech = content['details'][0]['speech']
                        sp_time = '已停留 ' + str(int(content['details'][0]['sptime'] / 1000 / 1000 / 60)) + ' 分钟'   # 分钟
                        dv = {
                            'bill_id': self.id,
                            'sequence': i,
                            'step': self.gen_sp_userid(sp_userid),
                            'item_status': _compute_state(sp_status),
                            'speech': sp_speech,
                            'sp_time': sp_time
                        }
                        record_obj.create(dv)
                        i += 1
        except Exception as e:
            _logger.error("获取审批状态失败:::" + str(e) + '审批编号:{}'.format(self.sp_no))
            return

    def object_approval_status(self):
        """查看结果"""
        view_id = self.env.ref('enterprise_wechat.wx_approval_obj_view_tree_1458').id
        model = self.env.context.get('active_model')    # 模型名
        active_ids = self.env.context.get('active_ids')
        line_id = self.env[model].browse(active_ids).id     # 提交审批数据记录ID
        model_id = self.env['ir.model'].search([('model', '=', model)]).id
        # 审批名称，审批名称如何找？
        approval_name = self.with_user(1).env['base']\
            .get_views([], {'action_id': line_id})
        print(approval_name)
        approval_id = self.env['wx.approval'].search([('model_id', '=', model_id), ('name', '=', approval_name)]).id
        return {
            'name': _('查看结果'),
            'view_mode': 'tree',
            'res_model': 'wx.approval.obj',
            'domain': [
                ('res', '=', '{},{}'.format(model, line_id)),
                ('approval_id', '=', approval_id)
            ],
            'type': 'ir.actions.act_window',
            'target': 'new',
            'view_id': False,
            'views': [(view_id, 'tree')],
        }


class WxApprovalRecordIds(models.Model):
    _name = 'wx.approval.record_ids'
    _description = '审批流程信息'

    bill_id = fields.Many2one('wx.approval.obj', string="审批单据", ondelete='cascade', help='关联主表')

    sequence = fields.Char(string='序号')
    step = fields.Char(string='节点')          # 申请人、审批人、抄送人
    item_status = fields.Char(string='审批状态')
    speech = fields.Char(string='审批意见')
    sp_time = fields.Char(string='操作时间')
