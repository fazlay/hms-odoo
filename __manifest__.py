# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Hospital Management System',
    'version': '1.3',
    'author': "Fazlay Rabbi",
    'sequence': 10,
    'description': """ 
    This is a custom module for hospital management system
I""",
    'depends': ['base','mail','product','web'],
    'data': [
    'security/ir.model.access.csv',
    'data/sequence.xml',
    'views/appointment_views.xml',
    'views/patient_tag_views.xml',
    'views/appointment_line_views.xml',
    'views/patient_views.xml',
    'views/menu.xml',
    'reports/reports.xml',
    'reports/custom_header.xml',
       
    ],

    'license': 'LGPL-3',
}
