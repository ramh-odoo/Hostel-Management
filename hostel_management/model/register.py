from odoo import models, fields

class TestModel(models.Model):
    _name = 'hostel.register'
    _description = "Hostel Registration"

    name = fields.Char('Name',required= True)
    description = fields.Text()
    password = fields.Char()
    postcode = fields.Char()
    date_availability : fields.Date()
    selling_price = fields.Float(required= True)
    room_sharing = fields.Integer()
    living_area = fields.Integer()
    garden = fields.Boolean()
    garden_area = fields.Integer()
