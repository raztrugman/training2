from odoo import fields, models

class ACourse(models.Model):
    _name = 'openacademy.course.model'
    
    course_name = fields.Char()
    session_ids = fields.One2many('session.model')
    course_level = fields.Selection([('1','Easy'),('2','Medium'),('3','Hard')], default='1', string="Course level")
