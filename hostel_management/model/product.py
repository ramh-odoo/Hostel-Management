#-*- coding: utf-8 -*-
from odoo import models,fields, api, _
from odoo.exceptions import ValidationError

class Prduct(models.Model):
    _name = "hostel.product"
    _description = "hostel.product"

    name = fields.Char(string="Name of the product")
    product_id = fields.Many2one('hostel.product')
    count = fields.Float(string="count of item")
    sequence = fields.Char(string="Sequence",required=True,copy=False,readonly=True,default=lambda self: _("New"))
    product_ids= fields.One2many('hostel.register', "product_id", "Student")


    @api.constrains("name")
    def _check_unique_field(self):
        for record in self:
            existing_records = self.search([("name","=",record.name)])
            if len(existing_records) > 1:
                raise ValidationError("Field Name must be unique!")
