from odoo.odoo import fields, models


class Books(models.Model):
    _name = "library.books"

    name = fields.Char(string="Book Title")
    author_ids = fields.Many2many("library.partners", string='Authors')
    edition_date = fields.Date()

    rental_ids = fields.One2many('library.rentals', 'book_id', string='Rentals')

