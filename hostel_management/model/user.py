#-*- coding: utf-8 -*-
from odoo import models, fields

class Users(models.Model):
    _inherit = 'res.users'
    _description = 'IsAdmin'

    student = fields.Boolean(string='Is Student')
    admin = fields.Boolean(string='Is Admin')
