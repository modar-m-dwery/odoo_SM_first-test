{
    "name": "School Management (test1)",
    "version": "16.0.1.0.0",
    "author": "Eng.Modar Dwery",
    "depends": ["contacts"],
    "data": [
        'security/user_groups.xml',
        'security/ir.model.access.csv',
        'views/admin/level_admin.xml',
        'views/admin/major_admin.xml',
        'views/admin/build_admin.xml',
        'views/admin/teacher_admin.xml',
        'views/admin/subject_admin.xml',
        'views/admin/student_admin.xml',
        'views/admin/room_class_admin.xml',

        # Dashboard Views

        # Reports
        
        # Sequences
        'data/ir_sequence_data.xml',

        # Menu
        'views/menu.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
