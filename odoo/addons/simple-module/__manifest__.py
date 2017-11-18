# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Vidange',
    ' '
    'version': '1.1',
    'category': 'Parc automobile',
    'sequence': 75,
    'summary': 'Vehicules, Vehicules Details',
    'description': """
gestion des Vehicules
==========================

This application enables you to manage important aspects of your company's staff and other details such as , contrat vehicules, conducteur ...


You can manage:
---------------
* Vehicules  : You can define your car with User and display hierarchies
* Vehicules
* Type
    """,
    'website': 'https://www.odoo.com',
    'images': [
        'images/Vehicules.jpeg',
        'images/Vehicules_employee.jpeg',
        'images/Vehicules_job_position.jpeg',
        'static/src/img/default_image.png',
    ],
    'depends': [
        'base_setup',
        'mail',
        'resource',
        'web_kanban',
    ],
    'data': [
        'security/hr_security.xml',
        'security/ir.model.access.csv',
        'views/hr_views.xml',
        'views/hr_templates.xml',
        'data/hr_data.xml',
    ],
    'demo': [
        'data/hr_demo.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
}
