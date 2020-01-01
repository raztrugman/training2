# -*- coding: utf-8 -*-
from odoo.odoo import fields, models, api


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Course'

    name = fields.Char(string='Title', required=True)
    description = fields.Text()

    responsible_id = fields.Many2one('openacademy.partner', string="Responsible")
    session_ids = fields.One2many('openacademy.session', 'course_id', string="Sessions")

    level = fields.Selection([('1', 'Easy'), ('2', 'Medium'), ('3', 'Hard')], string="Difficulty Level")


class Session(models.Model):
    _name = 'openacademy.session'
    _description = 'Session'

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    state = fields.Selection([('draft', "Draft"), ('confirmed', "Confirmed"), ('done', "Done")], default='draft')

    start_date = fields.Date(default=fields.Date.context_today)
    duration = fields.Float(digits=(6, 2), help="Duration in days", default=1)

    instructor_id = fields.Many2one('openacademy.partner', string="Instructor")
    course_id = fields.Many2one('openacademy.course', ondelete='cascade', string="Course", required=True)
    attendee_ids = fields.Many2many('openacademy.partner', string="Attendees")

    number_of_seats = fields.Integer()

    number_of_taken_seats = fields.Integer(compute='_check_max_capacity_for_session', store=True)

    @api.depends('number_of_seats', 'attendee_ids')
    def _check_max_capacity_for_session(self):
        for session in self:
            if not session.number_of_seats:
                session.number_of_taken_seats = 0
            else:
                session.number_of_taken_seats = len(session.attendee_ids)



