# # Mandatory
# from odoo import api, models, fields

# class Level(models.Model):
#   _name = 'school_management.level' 
#   _description = 'model tingkat' 
#   _rec_name = 'level'

#   level = fields.Selection([
#     ('10', '10'),
#     ('11', '11'),
#     ('12', '12')
# ], default=False, string='Tingkat')

from odoo import api, models, fields

class Level(models.Model):
    _name = 'school_management.level' 
    _description = 'Level Model' 
    _rec_name = 'level'

    level = fields.Selection([
        ('10', '10'),
        ('11', '11'),
        ('12', '12')
    ], default=False, string='Level')
