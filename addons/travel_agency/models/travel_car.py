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
    state = fields.Selection([
        ('draft', 'Draft'),
        ('running', 'Running')
    ], default='draft')

    _sql_constraints = [
        ('license_number_uniq', 'unique(license_number)', 'The name of the license_number must be unique !'),
    ]

    def name_get(self):
        return [(record.id, f"{record.license_number}({record.driver_id.name})") for record in self]

    def action_draft(self):
        self.state = 'draft'

    def action_running(self):
        self.state = 'running'

    def action_change_driver(self):
        return {
            "name": "Change Driver",
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "change.driver.wizard",
            "target": "new"
        }

    def action_show_driver_history(self):
        return {
            "name": f"{self.license_number}'s Driver History",
            "type": "ir.actions.act_window",
            "view_mode": "tree,form",
            "res_model": "driver.history",
            "target": "current",
            "domain": [('travel_car_id', '=', self.id)]
        }
