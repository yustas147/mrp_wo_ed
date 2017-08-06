# -*- coding: utf-8 -*-
{
    'name': "MRP MO editable",
    'author': "Simbioz, Yury Stasovsky",
    'license': 'LGPL-3',
    'website' : "https://simbioz.ua",
    'category': 'Manufacturing',
    'version': '1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['mrp'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'wizard/wiz_view.xml',
        'view.xml',
    ],
    'installable': True
}
