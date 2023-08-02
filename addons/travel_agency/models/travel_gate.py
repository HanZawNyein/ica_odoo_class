from odoo import models, fields


class TravelGate(models.Model):
    _name = "travel.gate"
    _description = "Travel Gate"

    name = fields.Char(required=True, readonly=False)
    township_id = fields.Many2one('travel.township')
