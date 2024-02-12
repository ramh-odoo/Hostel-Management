from odoo import models,fields,api

class HostelRoomsAllocation(models.Model):
    _name = 'hostel.roomallocation'
    _description = 'hostel.roomallocation '
    _rec_name = 'room_id'

    room_id = fields.Many2one('hostel.room',required=True,string="Room no")
    student_ids = fields.Many2many('hostel.register',domain="[('states', '=', 'confirmed')]",required=True)
    name = fields.Char('student_ids.name')
    sequence_number = fields.Char(string="sequence")
    start_date = fields.Date(string='from')
    end_date = fields.Date(string='To')
    room_type = fields.Selection(related='room_id.room_type')
    room_ac = fields.Boolean(related='room_id.room_ac')
    bath_attached = fields.Boolean(related='room_id.bath_attached')
    room_price = fields.Float(related='room_id.room_rate')
    mess_price = fields.Float(related='room_id.mess_rate')
    count = fields.Integer(compute='_compute_student_count', string='Number of Students')
    states = fields.Selection([('pending','Pending'),('confirmed','Confirmed'),('rejected','Rejected')],string='Status',default='pending')
