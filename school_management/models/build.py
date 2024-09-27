from odoo import api, models, fields

class Build(models.Model):
    _name = 'school_management.build' 
    _description = 'Building Model' 
    _rec_name = 'build'

    build = fields.Selection([
        ('general_building', 'General Building'),
        ('department_building', 'Department Building')
    ], default=False, string='Building')