# -*- coding: utf-8 -*-
{
    'name': "OpenACCM 企业微信应用模块",

    'summary': """
        企业微信应用模块""",

    'description': """
        企业微信应用模块，支持移动端应用场景
        更多支持：
        多度信息科技（南京）有限公司
        zou.jason@qq.com
    """,

    'author': "Jason Zou",
    'website': "http://www.open-accm.com/",

    'category': '企业微信接口',
    'version': '16.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'staff'],

    # always loaded
    'data': [
        'security/groups_security.xml',
        'security/ir.model.access.csv',
        'data/enterprise_wechat_data.xml',
        # 企业微信组织人员
        'views/ewi_res_company.xml',
        'views/ewi_staff_department.xml',
        'views/ewi_staff.xml',
        'views/ewi_interface.xml',
        'views/enterprise_wechat_menu.xml',
        # 企业微信审批流
        'views/wx_oa/wx_approval_views.xml',
        'views/wx_oa/wx_approval_record_views.xml',
        'views/wx_oa/wx_approval_obj_views.xml',
        'views/wx_oa/wechat_menu.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'AGPL-3',
}
