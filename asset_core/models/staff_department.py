# -*- coding: utf-8 -*-
"""
@Time    : 2022/11/11 00:50
@Author  : Jason Zou
@Email   : zou.jason@qq.com
"""
from odoo import models, fields, api, _
import logging
import os
_logger = logging.getLogger(__name__)
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


class StaffDepartment(models.Model):
    _inherit = 'staff.department'

    department_equipment_ids = fields.One2many('asset.core', 'department_id', string='部门设备', help='部门设备表')
