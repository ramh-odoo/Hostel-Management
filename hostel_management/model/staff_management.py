#-*- coding: utf-8 -*-
from odoo import models,fields, api

class HostelStaff(models.Model):
    _name = "hostel.staff"
    _description = "hostel.staff"

    name = fields.Char(string="Full name",required=True)
    email = fields.Char(string="Email",required=True)
    address = fields.Char(string="Address",required=True)
    city = fields.Char(string="City",required=True)
    state = fields.Selection([('select', 'Select'),('andhra_pradesh', 'Andhra Pradesh'),('arunachal_pradesh', 'Arunachal Pradesh'),('assam', 'Assam'),('bihar', 'Bihar'),
    ('chhattisgarh', 'Chhattisgarh'),('goa', 'Goa'),('gujarat', 'Gujarat'),('haryana', 'Haryana'),('himachal_pradesh', 'Himachal Pradesh'),
    ('jharkhand', 'Jharkhand'),('jk', 'Jammu and Kashmir'),('karnataka', 'Karnataka'),('kerala', 'Kerala'),('madhya_pradesh', 'Madhya Pradesh'),('maharastra', 'Maharastra'),('maharashtra', 'Maharashtra'),('manipur', 'Manipur'),
    ('meghalaya', 'Meghalaya'),('mizoram', 'Mizoram'),('nagaland', 'Nagaland'),('odisha', 'Odisha'),('punjab', 'Punjab'),('rajasthan', 'Rajasthan'),('sikkim', 'Sikkim'),
    ('tamil_nadu', 'Tamil Nadu'),('telangana', 'Telangana'),('tripura', 'Tripura'),('uttar_pradesh', 'Uttar Pradesh'),('uttarakhand', 'Uttarakhand'),('west_bengal', 'West Bengal')])
    contact = fields.Char(string="Contact",required=True)
    DOB = fields.Date(string="Date of birth",required=True)
    gender = fields.Selection([("Male","Male"),("Female","Female")],string = "Gender")
    marital_status = fields.Selection([("single","Single"),("married","Married"),])
    monthly_salary = fields.Char(string="Monthly Salary")
