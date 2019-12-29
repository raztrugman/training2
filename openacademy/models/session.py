from odoo.odoo import fields, models

class ASession(models.Model):
    _name = 'openacademy.session.model'
    
    session_date = fields.Char()

    course_id = fields.Many2one('course.model')
    instructor_id = fields.Many2one('instructor.model')
    active_session = fields.Boolean()
