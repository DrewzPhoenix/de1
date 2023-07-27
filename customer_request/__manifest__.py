{
    'name':"CRM Inherit",
    'version':'1.0.0',
    'Category':'CRM Inherit',
    'author':'Odoo Master',
    'sequence': -100,
    'website':'www.odoomaster.tech',
    'summary':'Odoo 13 development',
    'description':'CRM Inherit',
    'depends':['crm', 'sale_management', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/customer_request_view.xml',
        'views/customer_crm_view.xml'
    ],
    'demo': [],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}