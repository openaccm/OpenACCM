# -*- coding: utf-8 -*-
{
    'name': "OpenACCM 设备资产综合管控解决方案",

    'summary': """
    设备资产综合管控 Asset Comprehensiveness Control and Management
    """,

    'description': """设备资产综合管控基础模块
                    更多支持：
                    多度信息科技（南京）有限公司
                    zou.jason@qq.com
                    """,

    'author': "Jason Zou",
    'website': "http://www.open-accm.com/",

    'category': '设备资产综合管控',
    'version': '16.0.0.1',

    'depends': ['base', 'mail', 'partner_address', 'staff', 'buy', 'scm', 'auditlog', 'task', 'document_knowledge',
                'document_page', 'auto_backup', 'muk_web_theme'],

    'data': [
        'data/ir_sequence_data.xml',
        'data/asset_base_data.xml',
        'data/alarm_scheduler_data.xml',
        'data/task_alarm_data.xml',
        'security/groups.xml',
        'security/ir.model.access.csv',
        'security/rules.xml',
        'wizard/work_sheet_wizard_view.xml',
        'views/staff_department_view.xml',
        'views/asset_base_views.xml',
        'views/asset_core_views.xml',
        'views/asset_team_views.xml',
        'views/asset_core_line_views.xml',
        'views/work_sheet_management_views.xml',
        'views/asset_menu_views.xml',
        'views/templates.xml',
        'views/task_views.xml',
    ],
    'demo': [
        'demo/asset_core_demo.xml',
        'demo/task_alarm_demo.xml',
        'demo/asset_core_line_demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'asset_core/static/src/**/*',
        ]
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'AGPL-3',
}
