from odoo import api, models, fields

class Teacher(models.Model):
    _name = 'school_management.teacher' 
    _description = 'Teacher Model' 
    _rec_name = 'teacher_name'

    teacher_id = fields.Char(string="Teacher ID (NIP)", readonly=True, copy=False, default='New')
    teacher_name = fields.Char(string="Teacher Name", required=True)
    gender = fields.Selection([
        ('f', 'Female'),
        ('m', 'Male')
    ], string="Gender", default=False)

    active = fields.Boolean(string="Active", default=False)

    @api.model
    def create(self, vals):
        if vals.get('teacher_id', 'New') == 'New':
            sequence = self.env['ir.sequence'].next_by_code('school_management.teacher.sequence') or 'New'
            vals['teacher_id'] = sequence
        return super(Teacher, self).create(vals)



