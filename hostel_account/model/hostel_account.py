#-*- coding: utf-8 -*-

from odoo import models, fields,Command

class HostelAccount(models.Model):
    _inherit='hostel.register'

    def action_sold(self):
        res = super().action_sold()
        journal = self.env["account.journal"].search([("type", "=", "sale")], limit=1)
        print("----------------------", len(self))
        print(self.read())
        for prop in self:
            self.env["account.move"].create({"partner_id": prop.buyer_id.id,
                    "move_type": "out_invoice",
                    "journal_id": journal.id,
                    "invoice_line_ids": [Command.create({"name": prop.name,"quantity": 1.0,"price_unit": prop.selling_price}),
                        Command.create({"name": "Tax 6%","quantity": 1.0,"price_unit": prop.selling_price * 6.0 / 100.0}),
                        Command.create({"name": "Administrative fees","quantity": 1.0,"price_unit": 100.0})],
                    })
        return res
