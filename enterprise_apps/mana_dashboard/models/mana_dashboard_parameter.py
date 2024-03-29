
# -*- coding: utf-8 -*-

from odoo import models, fields, api
import pendulum


class ManaDashboardParameter(models.Model):
    '''
    Mana Dashboard Parameter
    '''
    _name = 'mana_dashboard.parameter'
    _description = 'Mana Dashboard Parameter'

    name = fields.Char(string='Name', required=True)

    data_source_mixin_id = fields.Many2one(
        string='Data Source Mixin',
        comodel_name='mana_dashboard.data_source_mixin',
        ondelete='cascade')
    
    type = fields.Selection(
        string='Type',
        selection=[
        ("date", "date"), 
        ("datetime", "datetime"), 
        ("float", "float"), 
        ("int", "int"), 
        ("char", "char")], default="char")
    
    logic_type = fields.Selection(
        string='Logic Type',
        selection=[
            ('and', 'and'), 
            ('or', 'or')], 
        default='and'
    )

    operator = fields.Selection(
        string='Operator', 
        selection = [
            ('=', '='), 
            ('!=', '!='),
            ('>', '>'),
            ('>=', '>='),
            ('<', '<'),
            ('<=', '<='),
            ('in', 'in'),
            ('not in', 'not in'),
            ('like', 'like'),
            ('not like', 'not like'),
            ('ilike', 'ilike'),
            ('not ilike', 'not ilike'),
            ('child_of', 'child_of'),
            ('parent_of', 'parent_of'),
            ('not child_of', 'not child_of'),
            ('not parent_of', 'not parent_of')], 
        default='=')
    
    default_value = fields.Char(string='Default Value')
    description = fields.Char(string='Description')

    def get_default_value(self):
        """
        get default value
        """
        self.ensure_one()

        default_val = self.default_value
        if self.type == 'date':
            default_val = pendulum.parse(default_val).to_date_string()
        elif self.type == 'datetime':
            default_val = pendulum.parse(default_val).to_datetime_string()
        elif self.type == 'float':
            default_val = float(default_val)
        elif self.type == 'int':
            default_val = int(default_val)

        return default_val
    
    def get_parameters(self):
        """
        get parameters
        """
        paramaters_dict = {}
        for parameter in self:
            paramaters_dict[parameter.name] = parameter.get_default_value()
        return paramaters_dict
