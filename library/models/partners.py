from odoo.odoo import fields, models


class Partners(models.Model):
    _name = "library.partners"

    name = fields.Char()
    email = fields.Char()
    address = fields.Char()
    type = fields.Selection([('customer', 'Customer'), ('author', 'Author')])

    rental_ids = fields.One2many('library.rentals', 'customer_id', string='Rentals')


