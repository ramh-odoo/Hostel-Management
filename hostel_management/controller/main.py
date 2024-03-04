# -*- coding: utf-8 -*-

from datetime import datetime
from odoo import http
from odoo.http import request

class Hostel(http.Controller):

    @http.route(['/students','/students/page/<int:page>'], auth='public', website=True)
    def students(self, page = 1, **kw):
        all_students = request.env['hostel.register'].search([])
        per_page = 8
        offset = (page -1 ) * per_page
        students = all_students[offset:offset + per_page]
        pager = http.request.website.pager(
            url='/students',
            total=len(all_students),
            page=page,
            step=per_page,
            scope=5,
        )
        return http.request.render('hostel_management.students_template', {
            'students' : students,
            'pager' : pager
        })

    @http.route("/students/<model('hostel.register'):student>", auth='public', website=True)
    def Main(self, student):
        return request.render('hostel_management.view_student_details', {'student' : student})

    @http.route(['/contact','/contactus'], auth='public', website=True)
    def contact(self, **kw):
        return http.request.render('hostel_management.contact_form_template',)


    @http.route('/submit_contact_form', type='http', auth="public", website=True, csrf=False)
    def submit_contact_form(self, **kwargs):
        name = kwargs.get('name')
        phone = kwargs.get('phone')
        email = kwargs.get('email')
        subject = kwargs.get('subject')
        question = kwargs.get('question')

        if name and phone and email and question:
            contact_data = {
                'name': name,
                'phone': phone,
                'email': email,
                'subject': subject,
                'question': question,
            }
            request.env['hostel.contact'].sudo().create(contact_data)

        return request.redirect('/contactus-thank-you')
