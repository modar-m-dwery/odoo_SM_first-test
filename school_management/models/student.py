from odoo import api, models, fields

class Student(models.Model):
    _name = 'school_management.student' 
    _description = 'Student Model' 
    _rec_name = 'student_name'

    student_id = fields.Char(string="Student ID (NIS)", readonly=True, copy=False, default='New')
    student_name = fields.Char(string="Student Name", required=True)
    gender = fields.Selection([
        ('f', 'Female'),
        ('m', 'Male')
    ], default=False, string='Gender', required=True)
    date_of_birth = fields.Date(string="Date of Birth", required=True)
    level = fields.Many2one(comodel_name='school_management.level', string='Level', required=True)
    major = fields.Many2one(comodel_name='school_management.major', string='Major', required=True)
    attendance_ids = fields.One2many(comodel_name='school_management.attendance', inverse_name='student_id')

    @api.model
    def create(self, vals):
        if vals.get('student_id', 'New') == 'New':
            sequence = self.env['ir.sequence'].next_by_code('school_management.student.sequence') or 'New'
            vals['student_id'] = sequence
        return super(Student, self).create(vals)