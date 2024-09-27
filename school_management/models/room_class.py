# from odoo import api, models, fields

# class RoomClass(models.Model):
#     _name = 'school_management.room_class' 
#     _description = 'model Ruangan Kelas' 
#     _rec_name = 'major'

#     room_id = fields.Char(string='Nomor Ruangan') 
#     level = fields.Many2one(comodel_name='school_management.level',string='Tingkat')
#     major = fields.Many2one(comodel_name='school_management.major',string='Jurusan')
#     subject_name = fields.Many2one(comodel_name='school_management.subject', string='Mata Pelajaran')
#     teacher_name = fields.Many2one(comodel_name='school_management.teacher',string='Nama Guru')
#     lesson_time = fields.Float(string="Jam Pembelajaran", default=1.0)
#     build = fields.Many2one(comodel_name='school_management.build',string='Gedung')
#     absensi_ids = fields.One2many(comodel_name='school_management.absensi', inverse_name='class_id')
#     status = fields.Selection([
#         ('rancangan', 'Rancangan'),
#         ('selesai', 'Selesai')
#     ], default="rancangan", string='Status', tracking=True)

#         # Notif Pedding
#     def rancangan_button(self):
#         self.status = 'rancangan'

#     def selesai_button(self):
#         self.status = 'selesai'

# class Absensi(models.Model):
#     _name = 'school_management.absensi' 
#     _description = 'model Ruangan Kelas' 
#     _rec_name = 'class_id'

#     class_id = fields.Many2one('school_management.room_class')
#     nis_id = fields.Char(string="NIS")
#     student_name = fields.Many2one(comodel_name='school_management.student', string="Nama Siswa")
#     state = fields.Selection([
#         ('hadir', 'Hadir'),
#         ('alfa', 'Alfa'),
#         ('sakit', 'Sakit'),
#         ('izin', 'Izin'),
#     ], string="Keterangan", default=False, required=True)
#     student_ids = fields.One2many(comodel_name='school_management.student', inverse_name='absensi_ids')

#     @api.onchange('student_name')
#     def set_student(self):
#         self.nis_id = self.student_name.nis_id






from odoo import api, models, fields

class RoomClass(models.Model):
    _name = 'school_management.room_class' 
    _description = 'Class Room Model' 
    _rec_name = 'major'

    room_id = fields.Char(string='Room Number') 
    level = fields.Many2one(comodel_name='school_management.level', string='Level')
    major = fields.Many2one(comodel_name='school_management.major', string='Major')
    subject_name = fields.Many2one(comodel_name='school_management.subject', string='Subject')
    teacher_name = fields.Many2one(comodel_name='school_management.teacher', string='Teacher Name')
    lesson_time = fields.Float(string="Lesson Hours", default=1.0)
    build = fields.Many2one(comodel_name='school_management.build', string='Building')
    attendance_ids = fields.One2many(comodel_name='school_management.attendance', inverse_name='class_id')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('finished', 'Finished')
    ], default="draft", string='Status', tracking=True)

    # Notification for Status
    def draft_button(self):
        self.status = 'draft'

    def finished_button(self):
        self.status = 'finished'


class Attendance(models.Model):
    _name = 'school_management.attendance' 
    _description = 'Attendance Model' 
    _rec_name = 'class_id'

    class_id = fields.Many2one('school_management.room_class', string='Class')
    student_id = fields.Char(string="Student ID (NIS)")
    student_name = fields.Many2one(comodel_name='school_management.student', string="Student Name")
    state = fields.Selection([
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('sick', 'Sick'),
        ('excused', 'Excused'),
    ], string="Remarks", default=False, required=True)
    attendance_count = fields.Integer(string='Total Attendance', compute='_compute_attendance_stats', store=True)
    # student_ids = fields.One2many(comodel_name='school_management.student', inverse_name='attendance_ids')

    @api.onchange('student_name')
    def set_student(self):
        self.student_id = self.student_name.student_id

    # @api.depends('student_name')
    # def _compute_attendance_count(self):
    #     for record in self:
    #         record.attendance_count = len(record.student_name)
    