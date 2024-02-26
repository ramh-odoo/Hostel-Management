#-*- coding: utf-8 -*-
from odoo import models,fields, api, _
from odoo.exceptions import ValidationError

class Prduct(models.Model):
    _name = "hostel.service"
    _description = "hostel.service"

    name = fields.Char(string="Service")
    price = fields.Float(string="Price (per month)")
    sequence = fields.Char(string="Sequence",required=True,copy=False,readonly=True,default=lambda self: _("New"))
    student_ids=fields.Many2many('hostel.register',string='Student')
    active = fields.Boolean(default=True)

    @api.constrains("name")
    def _check_unique_field(self):
        for record in self:
            existing_records = self.search([("name","=",record.name)])
            if len(existing_records) > 1:
                raise ValidationError("Field Name must be unique!")
