#-*- coding: utf-8 -*-
from odoo import models,fields

class HostelStaff(models.Model):
    _name = 'hostel.staff'
    _description = 'hostel.staff'

    name = fields.Char(string='Full name',required=True)
    email = fields.Char(string='Email',required=True)
    address = fields.Char(string='Address',required=True)
    city = fields.Char(string='City',required=True)
    state = fields.Selection([('kerala','Kerala'),
    ('goa','Goa'),
    ('maharastra','Maharastra'),
    ('JK','Jammu and Kashmir'),
    ])
    contact = fields.Char(string='Contact',required=True)
    DOB = fields.Date(string='Date of birth',required=True)
    gender = fields.Selection([('Male','Male'),('Female','Female')],string = 'Gender')
    marital_status = fields.Selection([('single','Single'),
    ('married','Married'),])
    monthly_salary = fields.Char(string='Monthly Salary',required=True)
