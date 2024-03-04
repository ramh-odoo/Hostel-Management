#-- coding: utf-8 --
#Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Hostel Management",
    "description": "A comprehensive Hostel management system that enables guests to effortlessly manage hostel.",
    "summary": "Hostel management system",
    "category": "industry/real estate",
    "installable": True,
    "application": True,
    "license": "OEEL-1",
    "version": "1.0",
    "depends": ["base","website"],
    "data": [
        "security/user.xml",
        "security/ir.model.access.csv",
        "report/student_report.xml",
        "wizard/add_service_wizard.xml",
        "report/student_report_template.xml",
        "data/website_menu.xml",
        "views/student_template.xml",
        "views/contact_template.xml",
        "views/hostel_contact_view.xml",
        "views/hostel_room.xml",
        "views/hostel_register.xml",
        "views/hostel_staff.xml",
        "views/hostel_service.xml",
        "views/hostel_menus.xml",
    ],
}
