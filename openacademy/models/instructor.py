from odoo.odoo import fields, models

class AInstructor(models.Model):
    _name = 'openacademy.instructor.model'
    
    instructor_name = fields.Char()

    session_ids = fields.One2many('session.model')
