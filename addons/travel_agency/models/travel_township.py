from odoo import api, fields, models


class TravelTownship(models.Model):
    _name = 'travel.township'
    _description = 'TravelTownship'

    name = fields.Char()
    travel_gate_ids = fields.One2many('travel.gate', 'township_id')

    # _sql_constraints = [
    #     ('name_unique', 'unique(name)', 'The name of the Township must be unique !'),
    # ]
