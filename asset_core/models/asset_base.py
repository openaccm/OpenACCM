# -*- coding: utf-8 -*-
"""
@Time    : 2023/02/24 16:44
@Author  : Jason Zou
@Email   : zou.jason@qq.com
"""
from odoo import models, fields, api, _
import logging
import os
from random import randint
_logger = logging.getLogger(__name__)
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


class AssetTag(models.Model):
    _name = 'asset.tag'
    _description = '设备标签'

    def _get_default_color(self):
        return randint(1, 11)

    name = fields.Char('标签名称', translate=True)
    color = fields.Integer('颜色', default=_get_default_color)
    active = fields.Boolean('待归档', default=True)
    company_id = fields.Many2one(
        'res.company',
        string='公司',
        change_default=True,
        default=lambda self: self.env.company)


class AssetTaskType(models.Model):
    _name = "asset.task.type"
    _description = "工单类"
    _order = "id"

    name = fields.Char(string='名称', required=True)
    active = fields.Boolean(string="启用", default=True)
    company_id = fields.Many2one(
        'res.company',
        string='公司',
        change_default=True,
        default=lambda self: self.env.company)
