from odoo import models,fields

class HostelStockLine(models.Model):
    _name ='hostel.stock.line'
    _description = 'hostel Stockline'
    _rec_name = 'inventory_id'

    inventory_id = fields.Many2one('hostel.inventory',string='product')
    qty = fields.Float(string='qty')
    uom = fields.Selection(related='inventory_id.uom')
    stock_id = fields.Many2one('hostel.stock')

class StockManagement(models.Model):
    _name = 'hostel.stock'
    _description = 'hostel.stock'
    _rec_name = 'sequence'

    inventory_type = fields.Selection([('Incom','Incoming'),('Outgo','Outgoing')],string='Inventory Type' ,required = True)
    date = fields.Datetime(string='Date', required=True)
    sequence = fields.Char(string='Sequence',required=True,copy=False,readonly=True,default=lambda self: _('New'))
    line_ids = fields.One2many('hostel.stock.line','stock_id',required=True)
    status = fields.Selection([('pending','Pending'),('updated','Updated')],string='Status', default='pending', required = True)
