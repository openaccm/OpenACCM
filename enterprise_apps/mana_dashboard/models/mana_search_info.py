
# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools
import json5
import pendulum

class RangeHelper:
    """
    Range Helper
    """
    def __init__(self, range_info):
        self.range_info = range_info
        self.range_type = range_info['range_type']

    def get_start_end(self):
        """
        get start and end
        """
        start_time = None
        end_time = None
        range_type = self.range_type.lower()
        if range_type == 'custom range':
            start_time = pendulum.parse(self.range_info['start'])
            end_time = pendulum.parse(self.range_info['end'])
        elif range_type == 'today':
            start_time = pendulum.now().start_of('day')
            end_time = pendulum.now().end_of('day')
        elif range_type == 'yesterday':
            start_time = pendulum.now().subtract(days=1).start_of('day')
            end_time = pendulum.now().subtract(days=1).end_of('day')
        elif range_type == 'tomorrow':
            start_time = pendulum.now().add(days=1).start_of('day')
            end_time = pendulum.now().add(days=1).end_of('day')
        elif range_type == 'this week':
            start_time = pendulum.now().start_of('week')
            end_time = pendulum.now().end_of('week')
        elif range_type == 'this month':
            start_time = pendulum.now().start_of('month')
            end_time = pendulum.now().end_of('month')
        elif range_type == 'this quarter':
            quarter = pendulum.now().quarter
            if quarter == 1:
                start_time = pendulum.now().start_of('year')
                end_time = pendulum.now().add(months=2).end_of('month')
            elif quarter == 2:
                start_time = pendulum.now().add(months=3).start_of('month')
                end_time = pendulum.now().add(months=5).end_of('month')
            elif quarter == 3:
                start_time = pendulum.now().add(months=6).start_of('month')
                end_time = pendulum.now().add(months=8).end_of('month')
            elif quarter == 4:
                start_time = pendulum.now().add(months=9).start_of('month')
                end_time = pendulum.now().end_of('year')
        elif range_type == 'this year':
            start_time = pendulum.now().start_of('year')
            end_time = pendulum.now().end_of('year')
        elif range_type == 'last month':
            start_time = pendulum.now().subtract(months=1).start_of('month')
            end_time = pendulum.now().subtract(months=1).end_of('month')
        elif range_type == 'last quarter':
            quarter = pendulum.now().quarter
            if quarter == 1:
                start_time = pendulum.now().subtract(years=1).add(months=9).start_of('month')
                end_time = pendulum.now().subtract(years=1).end_of('year')
            elif quarter == 2:
                start_time = pendulum.now().start_of('year')
                end_time = pendulum.now().add(months=2).end_of('month')
            elif quarter == 3:
                start_time = pendulum.now().add(months=3).start_of('month')
                end_time = pendulum.now().add(months=5).end_of('month')
            elif quarter == 4:
                start_time = pendulum.now().add(months=6).start_of('month')
                end_time = pendulum.now().add(months=8).end_of('month')
        elif range_type == 'last year':
            start_time = pendulum.now().subtract(years=1).start_of('year')
            end_time = pendulum.now().subtract(years=1).end_of('year')
        elif range_type == 'last week':
            start_time = pendulum.now().subtract(weeks=1).start_of('week')
            end_time = pendulum.now().subtract(weeks=1).end_of('week')
        elif range_type == 'last 7 days':
            start_time = pendulum.now().subtract(days=7)
            end_time = pendulum.now()
        elif range_type == 'last 30 days':
            start_time = pendulum.now().subtract(days=30)
            end_time = pendulum.now()
        elif range_type == 'last 90 days':
            start_time = pendulum.now().subtract(days=90)
            end_time = pendulum.now()
        elif range_type == 'last 180 days':
            start_time = pendulum.now().subtract(days=180)
            end_time = pendulum.now()
        elif range_type == 'last 365 days':
            start_time = pendulum.now().subtract(days=365)
            end_time = pendulum.now()
        elif range_type == 'next week':
            start_time = pendulum.now().add(weeks=1).start_of('week')
            end_time = pendulum.now().add(weeks=1).end_of('week')
        elif range_type == 'next 7 days':
            start_time = pendulum.now()
            end_time = pendulum.now().add(days=7)
        elif range_type == 'next 30 days':
            start_time = pendulum.now()
            end_time = pendulum.now().add(days=30)
        elif range_type == 'next 90 days':
            start_time = pendulum.now()
            end_time = pendulum.now().add(days=90)
        elif range_type == 'next 180 days':
            start_time = pendulum.now()
            end_time = pendulum.now().add(days=180)
        elif range_type == 'next 365 days':
            start_time = pendulum.now()
            end_time = pendulum.now().add(days=365)
        elif range_type == 'next month':
            start_time = pendulum.now().add(months=1).start_of('month')
            end_time = pendulum.now().add(months=1).end_of('month')
        elif range_type == 'next quarter':
            quarter = pendulum.now().quarter
            if quarter == 1:
                start_time = pendulum.now().add(months=3).start_of('month')
                end_time = pendulum.now().add(months=5).end_of('month')
            elif quarter == 2:
                start_time = pendulum.now().add(months=6).start_of('month')
                end_time = pendulum.now().add(months=8).end_of('month')
            elif quarter == 3:
                start_time = pendulum.now().add(months=9).start_of('month')
                end_time = pendulum.now().end_of('year')
            elif quarter == 4:
                start_time = pendulum.now().add(years=1).start_of('year')
                end_time = pendulum.now().add(years=1).add(months=2).end_of('month')
        elif range_type == 'next year':
            start_time = pendulum.now().add(years=1).start_of('year')
            end_time = pendulum.now().add(years=1).end_of('year')
        elif range_type == 'all time':
            start_time = False
            end_time = False
        else:
            raise Exception('invalid range type')

        return start_time, end_time
        

class SearchInfoHelper:
    """
    a helper class to handle search info
    """

    def __init__(self, env, search_infos):
        self.env = env
        self.search_infos = json5.loads(search_infos)
        global_search_infos = []
        for search_info in self.search_infos:
            if search_info.get('type') == 'global':
                global_search_infos.append(search_info)
        self.global_search_infos = global_search_infos
        config_search_infos = {}
        for search_info in self.search_infos:
            targets = search_info.get('targets', [])
            for target in targets:
                config_search_infos[target].setdefault('search_infos', []).append(search_info)
        self.config_search_infos = config_search_infos

    @property
    def has_global_search(self):
        for search_info in self.search_infos:
            if search_info['is_global']:
                return True
        return False

    def get_global_search_infos(self):
        return self.global_search_infos

    def get_search_infos(self, any_config_id):
        """
        get search info by config id
        """
        global_search_infos = self.get_global_search_infos()
        config_search_infos = self.config_search_infos.get(any_config_id, [])
        return global_search_infos + config_search_infos

    def get_time_ranges(self, config_id):
        """
        get time ranges from search info
        """
        search_infos = self.get_search_info_by_config(config_id)
        if not search_infos:
            return None, None

        time_ranges = []
        for search_info in search_infos:
            if search_info['type'] == 'date_range':
                time_ranges.append(search_info)

        start_time = None
        end_time = None
        for time_range in time_ranges:
            _start_time, _end_time = self._get_time_range(time_range)
            if not start_time:
                start_time = _start_time
            else:
                start_time = max(start_time, _start_time) 
            if not end_time:
                end_time = _end_time
            else:
                end_time = min(end_time, _end_time)

        if start_time:
            start_time = start_time.format('YYYY-MM-DD HH:mm:ss')
        if end_time:
            end_time = end_time.format('YYYY-MM-DD HH:mm:ss')

        return start_time, end_time

    def _get_time_range(self, range_info):
        """
        range helper
        """
        helper = RangeHelper(range_info)
        return helper.get_start_end()
            

class ManaDashboardSearchInfo(models.Model):
    '''
    Search Info
    '''
    _name = 'mana_dashboard.search_info'
    _description = 'Mana Dashboard Search Info'

    uid = fields.Many2one(string='uid', comodel_name='res.users')
    dashboard_id = fields.Many2one(string='dashboard_id', comodel_name='mana_dashboard.dashboard')

    search_config_id = fields.Many2one(
        string='Search Config', 
        comodel_name='mana_dashboard.any_config',
        ondelete='cascade')
    
    search_infos = fields.Text(string='search infos')
    targets = fields.Many2many(
        string='targets', comodel_name='mana_dashboard.any_config')

    @tools.ormcache('self.env.uid', 'dashboard_id')
    def get_search_info_helper(self, dashboard_id):
        """
        get search info helper
        """
        record = self.env['mana_dashboard.search_info'].search([
            ('dashboard_id', '=', dashboard_id),
            ('uid', '=', self.env.uid)
        ], limit=1)
        if record and record.search_infos:
            return SearchInfoHelper(self.env, record.search_infos)
        else:
            return SearchInfoHelper(self.env, '[]')
        
    def reset_search_infos(self, dashboard_id):
        """
        reset search info
        """
        records = self.env['mana_dashboard.search_info'].search([
            ('dashboard_id', '=', dashboard_id),
            ('uid', '=', self.env.uid)
        ])
        records.unlink()
        self.clear_caches()
        