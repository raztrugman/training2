# -*- coding: utf-8 -*-, api
from odoo import fields, models


class Partner(models.Model):
    """
    _name = 'openacademy.partner'
    _description = 'Partner'

    name = fields.Char()
    """

    _inherit = 'res.partner'

    instructor = fields.Boolean(default=False)
    session_ids = fields.Many2many('openacademy.session', string="Attended Sessions", readonly=True)




