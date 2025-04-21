from odoo import models, fields # type: ignore

class TCUStudent(models.Model):
    _name = 'tcu.student'
    _description = 'TCU Student'
    
    name = fields.Char(string='Student Name', required=True)
    email = fields.Char(string='Email')
    carrera = fields.Char(string='Career')
    student_id = fields.Char(string='Student ID', required=True)
    university = fields.Char(string='University')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], string='Status', default='draft')