#-*- coding: utf-8 -*-

from odoo import models, fields, api

class AddServiceWizard(models.TransientModel):
    _name = 'hostel.add.service.wizard'
    _description = 'hostel.add.service.wizard'

    service_ids=fields.Many2many('hostel.service')

    def add_service(self):
        active_ids = self.env.context.get('active_ids')
        students = self.env['hostel.register'].browse(active_ids)
        for student in students:
            student.write({
                'service_ids': [(4, service.id) for service in self.service_ids]
            })
