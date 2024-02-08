from odoo import models, fields

class TestModel(models.Model):
    _name = 'hostel.register'
    _description = "Hostel Registration"

    name = fields.Char (string = 'First Name', required = True) 
    last_name = fields.Char (string = 'Last Name', required = True)
    email= fields.Char (string = 'Email Address',required = True)
    permanent_address = fields.Char (string = 'Permanent Address')
    date_of_birth = fields.Date (string = 'Date Of Birth')
    city = fields.Char (string = 'City')
    permanent_address = fields.Char (string = 'Permanent Address',required = True)
    date_of_birth = fields.Date (string = 'Date Of Birth',required = True)
    city = fields.Char (string = 'City',required = True)
