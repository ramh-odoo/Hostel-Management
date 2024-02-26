#-*- coding: utf-8 -*-
from odoo import models,fields, api
from odoo.exceptions import ValidationError

class HostelRooms(models.Model):
    _name = "hostel.room"
    _description = "hostel.room"
    _rec_name = "room_no"
    _default_view='view_hostel_room_form'

    room_no = fields.Char(string="Room number")
    sequence_number = fields.Char(string = "id")
    room_type = fields.Selection([("2share","2 share"),("3share","3 share"),("4share","4 share")],string="Type of room",required=True)
    room_ac = fields.Boolean(string="Ac room", default=True)
    count = fields.Integer(string="Count of people", compute='_compute_people_count', store=True)
    bath_attached = fields.Boolean(string="Bathroom attached",default=True)
    availability = fields.Boolean(string="Room availability")
    room_rate = fields.Float( string="Room Price",store=True)
    mess_rate = fields.Float( string="Mess Price",store=True)
    start_date = fields.Date(string="from")
    end_date = fields.Date(string="To")
    status = fields.Selection([("pending","Pending"),("confirmed","Confirmed"),("rejected","Rejected")],string="Status",default="pending")
    student_ids = fields.Many2many("hostel.register",required=True)
    name = fields.Char("student_ids.name")

    @api.depends('student_ids')
    def _compute_people_count(self):
        self.count=len(self.student_ids)

    @api.depends('student_ids')
    def check_room_type_limit(self):
        if self.room_type == '2share' and len(self.student_ids) > 2:
            raise ValidationError("Cannot add more than two students for 2 share room type.")
        elif self.room_type == '3share' and len(self.student_ids) > 3:
            raise ValidationError("Cannot add more than three students for 3 share room type.")
        elif self.room_type == '4share' and len(self.student_ids) > 4:
            raise ValidationError("Cannot add more than four students for 4 share room type.")

    @api.onchange('room_type')
    def check_room_type_limit(self):
        if self.student_ids and len(self.student_ids) > int(self.room_type[0]):
            raise ValidationError(f"Cannot change room type to {self.room_type} with {len(self.student_ids)} students. Remove excess students first.")

    @api.onchange("room_type", "count")
    def _check_count_with_room_type(self):
        for record in self:
            if record.room_type == "2share" and record.count > 2:
                raise ValidationError("count of people must be 2 or below 2")
            elif record.room_type == "3share" and record.count > 3:
                raise ValidationError("count of people must be 3 or below 3")
            elif record.room_type == "4share" and record.count > 4:
                raise ValidationError("count of people must be 4 or below 4")

    @api.constrains("room_no")
    def _check_unique_field(self):
        for record in self:
            existing_records = self.search([("room_no", "=", record.room_no)])
            if len(existing_records) > 1:
                raise ValidationError("room number must be unique!")

    # @api.model
    # def create(self, vals):
    #     vals['sequence_number'] = self.env['ir.sequence'].next_by_code('hostel.room')
    #     return super(HostelRooms, self).create(vals)
