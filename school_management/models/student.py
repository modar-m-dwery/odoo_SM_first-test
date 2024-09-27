# Mandatory
# from odoo import api, models, fields

# class Siswa(models.Model):
#   _name = 'school_management.student' 
#   _description = 'model Murid' 
#   _rec_name = 'student_name'

#   nis_id = fields.Char(string="NIS")
#   student_name = fields.Char(string="Nama Siswa", required=True)
#   gender = fields.Selection([
#       ('p', 'Perempuan'),
#       ('l', 'Laki - Laki')
#   ], default=False, string='Jenis Kelamin', required=True)
#   date_of_birth = fields.Date(string="Tanggal Lahir", required=True)
#   level = fields.Many2one(comodel_name='school_management.level',string='Tingkat', required=True)
#   major = fields.Many2one(comodel_name='school_management.major',string='Jurusan', required=True)
#   absensi_ids = fields.One2many(comodel_name='school_management.absensi', inverse_name='student_ids')





from odoo import api, models, fields
import io
from odoo import http
from odoo.http import request
import xlsxwriter


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
    

    def generate_report(self):
        return self.env.ref('school_management.student_report_pdf').report_action(self)

    # def generate_excel_report(self):
    #     output = io.BytesIO()
    #     workbook = xlsxwriter.Workbook(output)
    #     worksheet = workbook.add_worksheet('Students')

    #     # Write headers
    #     headers = ['Student ID', 'Student Name', 'Attendance']
    #     for col, header in enumerate(headers):
    #         worksheet.write(0, col, header)

    #     # Write data
    #     row = 1
    #     for student in self:
    #         worksheet.write(row, 0, student.student_id)
    #         worksheet.write(row, 1, student.student_name)
    #         worksheet.write(row, 2, len(student.attendance_ids))
    #         row += 1

    #     workbook.close()
    #     output.seek(0)
        
    #     response = request.make_response(
    #         output.read(),
    #         headers=[
    #             ('Content-Disposition', 'attachment; filename=students_report.xlsx'),
    #             ('Content-Type', 'application/vnd.ms-excel')
    #         ]
    #     )
    #     return response