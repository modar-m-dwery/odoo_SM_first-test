from odoo import api, models, fields

class Subject(models.Model):
    _name = 'school_management.subject' 
    _description = 'Subject Model' 
    _rec_name = 'subject_name'

    subject_type = fields.Selection([
        ('g', 'General'),
        ('m', 'Major'),
    ], default=False, string='Subject Type')
    subject_name = fields.Char(string="Subject Name")


