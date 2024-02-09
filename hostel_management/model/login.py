#-*- coding: utf-8 -*-
from odoo import models, fields

class TestModel(models.Model):
    _name = 'hotsel.login'
    _description = "Hostel Login"

    name = fields.Char(required = True)
    password = fields.Char()
