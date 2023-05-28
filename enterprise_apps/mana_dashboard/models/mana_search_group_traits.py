
# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools

help_html = '''<div class="alert alert-info" role="alert">
    <p>If it is global, it will be applied to all the targets.</p>
    <p>If it is specified, it will be applied to the targets you selected.</p>
    <ul>
'''

class ManaDashboardSearchContainerTraits(models.Model):
    '''
    Mana Dashboard Search Container Traits
    '''
    _name = 'mana_dashboard.search_group_traits'
    _description = 'Search Group Trait'

    targets = fields.Many2many(
        string='Targets',
        comodel_name='mana_dashboard.any_config',
        relation='mana_search_group_traits_targets_rel')
    
    type = fields.Selection(
        string='Type',
        selection=[("specified", "specified"), ("global", "global")], 
        default="global")
    
    any_config_id = fields.Many2one(
        string='Config Id', 
        comodel_name='mana_dashboard.any_config')
    
    dashboard_id = fields.Many2one(
        string='Dashboard Id', 
        comodel_name='mana_dashboard.dashboard',
        related='any_config_id.dashboard_id', 
        store=True)
    
    search_immidiate = fields.Boolean(
        string='Immidiate', default=True)

    help = fields.Html(string='Help', default=help_html)
