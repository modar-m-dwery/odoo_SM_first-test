from odoo import api, models, fields

class Build(models.Model):
    _name = 'school_management.build' 
    _description = 'Building Model' 
    _rec_name = 'build'

    build = fields.Selection([
        ('general_building', 'General Building'),
        ('department_building', 'Department Building')
    ], default=False, string='Building')


# access_sm_teacher_admin,access_sm_teacher_admin,model_school_management_teacher,base.group_user,1,1,1,1
# access_sm_student_admin,access_sm_student_admin,model_school_management_student,base.group_user,1,1,1,1
