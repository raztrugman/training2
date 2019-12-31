from odoo import fields, models


class Rentals(models.Model):
    _name = 'library.rentals'

    book_id = fields.Many2many('library.books', 'Book')
    customer_id = fields.Many2many('library.partners', 'Customer')

    rent_book_date = fields.Date()
    return_book_date = fields.Date()


