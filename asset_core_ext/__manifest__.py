# -*- coding: utf-8 -*-
{
    'name': "OpenACCM 设备资产综合管控扩展应用",

    'summary': """设备资产综合管控扩展应用，去掉一些多余的菜单""",

    'description': """设备资产综合管控扩展应用
                    更多支持：
                    多度信息科技（南京）有限公司
                    zou.jason@qq.com
                    """,

    'author': "Jason Zou",
    'website': "http://www.open-accm.com/",

    'category': '设备资产综合管控',
    'version': '16.0.0.1',

    'depends': ['asset_core'],

    'data': [
        'views/asset_ext_menu_views.xml',
    ],
    'demo': [

    ],
    'assets': {

    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'AGPL-3',
}
