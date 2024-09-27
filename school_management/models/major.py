from odoo import api, models, fields

class Major(models.Model):
    _name = 'school_management.major' 
    _description = 'Major Model' 
    _rec_name = 'major'

    major = fields.Char(string='Major')
