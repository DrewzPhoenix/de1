from odoo import api,fields,models

class Lead(models.Model):
    _inherit = "crm.lead"

    request_ids = fields.One2many('crm.customer.request','opportunity_id',string='Request ID')
    # atest = fields.Char(string='name')
    total_sale = fields.Float(string='Total Sale', compute='_compute_total_sale')
    
    def _compute_total_sale(self):
        for lead in self:
            total_qty = 0.0
            for request in lead.customer_requests:
                total_qty += request.qty

            lead.total_sale = total_qty 