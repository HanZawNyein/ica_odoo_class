from odoo import api, fields, models


class TravelAgency(models.Model):
    _name = 'travel.agency'
    _description = 'TravelAgency'

    name = fields.Char(required=True)
    travel_car_ids = fields.One2many('travel.car', 'travel_agency_id')
