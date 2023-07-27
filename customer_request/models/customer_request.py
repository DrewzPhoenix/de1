from odoo import api,fields,models

class CustomerRequest(models.Model):
    # _name = "crm.lead.inherit"
    # _inherit="crm.lead"
    _name = "crm.customer.request"
    _description = "Customer Request"



    product_id = fields.Many2one('product.template',string="Product ID")
    opportunity_id= fields.Many2one('crm.lead',string="Opportunity ID")
    description=fields.Char(string='Description')
    date =fields.Date(string='Date',default=fields.Date.context_today)
    qty =fields.Float(string='Quantity')