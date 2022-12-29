# -*- coding: utf-8 -*-
{
    'name': 'Tourism',
    'version': '1.0',
    'author': 'Deependra Solanki',
    'summary': 'Tourism Booking',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/tourism_menus.xml',
        'views/tourism_places_views.xml',
        'views/tourism_hotels_views.xml',
        'views/tourism_activities_views.xml',
        'views/tourism_cars_views.xml'
    ],
    'demo': [
        'demo/tourism_places_demo_data.xml',
        'demo/tourism_hotels_demo_data.xml',
        'demo/tourism_activities_demo_data.xml',
        'demo/tourism_cars_demo_data.xml',
    ],
    'installable': True,
    'application': True,
}