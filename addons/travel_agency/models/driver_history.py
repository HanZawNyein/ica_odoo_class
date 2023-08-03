from odoo import api, fields, models


class DriverHistory(models.Model):
    _name = 'driver.history'
    _description = 'DriverHistory'
    _rec_name = "driver_id"

    driver_id = fields.Many2one('res.partner')
    join_date = fields.Date()
    fired_date = fields.Date()
    travel_car_id = fields.Many2one('travel.car')
    travel_agency_id = fields.Many2one('travel.agency', related="travel_car_id.travel_agency_id")
