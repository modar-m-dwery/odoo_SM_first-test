# # Mandatory
# from odoo import api, models, fields

# class Student(models.Model):
#   _name = 'school_management.subject' 
#   _description = 'model Mata Pelajaran' 
#   _rec_name = 'subject_name'


#   subject_type = fields.Selection([
#       ('u', 'Umum'),
#       ('j', 'Jurusan'),
#   ], default=False, string='Tipe Mata Pelajaran')
#   subject_name = fields.Char(string="Nama Mata Pelajaran")



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


