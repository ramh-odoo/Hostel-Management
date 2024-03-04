#-*- coding: utf-8 -*-

from odoo import fields, models, Command
class StudentFees(models.Model):
    _inherit='hostel.register'

    def state_confirmed(self):
        res = super().state_confirmed()
        journal = self.env["account.journal"].search([("type", "=", "sale")], limit=1)
        for prop in self:
            months =0
            if prop.room_id.start_date and prop.room_id.end_date:
                from_date = fields.Date.from_string(prop.room_id.start_date)
                to_date = fields.Date.from_string(prop.room_id.end_date)
                months = (to_date.year - from_date.year) * 12 + to_date.month - from_date.month
                if to_date.day >= from_date.day:
                    months += 1

            if not months:
                months =1

            vals = [Command.create({"name": "Room Rent","quantity": months,"price_unit": prop.room_id.room_rate}),
                        Command.create({"name": "Mess Fee","quantity": months,"price_unit": prop.room_id.mess_rate}),
                        Command.create({"name": "Tax 6%","quantity": 1.0,"price_unit": prop.room_id.mess_rate + prop.room_id.room_rate + 1000 * 6.0 / 100.0})
                        ]

            if prop.room_id.room_ac:
                vals.append(Command.create({"name": "AC ","quantity": months,"price_unit": 1000}))

            if prop.service_ids:
                for service in prop.service_ids:
                    vals.append(Command.create({'name' : service.name, 'quantity': months, 'price_unit' : service.price}))

            self.env["account.move"].create({"partner_id": prop.id,
                    "move_type": "out_invoice",
                    "journal_id": journal.id,
                    "invoice_line_ids": vals,
                    })
        return res
