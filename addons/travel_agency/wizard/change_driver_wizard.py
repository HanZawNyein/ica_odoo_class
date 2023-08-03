from odoo import api, fields, models, _
from odoo.exceptions import UserError


class ChangeDriverWizard(models.TransientModel):
    _name = 'change.driver.wizard'
    _description = 'ChangeDriverWizard'

    driver_id = fields.Many2one('res.partner')
    join_date = fields.Date()

    def action_change_driver(self):
        active_model = self.env.context.get('active_model')
        active_id = self.env.context.get('active_id')
        travel_id = self.env[active_model].browse(active_id)
        if travel_id.driver_id == self.driver_id:
            raise UserError(_("Driver Should not be same!"))
        values = {
            "travel_car_id": travel_id.id,
            "driver_id": travel_id.driver_id.id,
            "join_date": travel_id.join_date,
            "fired_date": fields.Date.today()
        }
        self.env['driver.history'].create(values)
        travel_id.driver_id = self.driver_id
        travel_id.join_date = self.join_date
