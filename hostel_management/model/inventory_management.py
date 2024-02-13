#-*- coding: utf-8 -*-
from odoo import models,fields
from odoo.exceptions import ValidationError

class HostelRoomInventory(models.Model):
    _name = "hostel.inventory"
    _description = "hostel.inventory"

    name = fields.Char(string="Name of the product")
    count = fields.Float(string="count of item",readonly=True)
    sequence = fields.Char(string="Sequence",required=True,copy=False,readonly=True,default=lambda self: _("New"))

    @api.constrains("name")
    def _check_unique_field(self):
        for record in self:
            existing_records = self.search([("name","=",record.name)])
            if len(existing_records) > 1:
                raise ValidationError("Field Name must be unique!")
