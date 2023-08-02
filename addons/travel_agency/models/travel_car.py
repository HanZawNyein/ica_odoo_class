from odoo import api, fields, models


class TravelCar(models.Model):
    _name = 'travel.car'
    _description = 'TravelCar'
    _order = "id desc"
    # _rec_name = "license_number"

    license_number = fields.Char()
    driver_id = fields.Many2one('res.partner')
    join_date = fields.Date()
    travel_agency_id = fields.Many2one('travel.agency')

    _sql_constraints = [
        ('license_number_uniq', 'unique(license_number)', 'The name of the license_number must be unique !'),
    ]

    def name_get(self):
        return [(record.id, f"{record.license_number}({record.driver_id.name})") for record in self]
