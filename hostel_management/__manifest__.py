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
    "depends": ["base"],
    "data": [
        "security/user.xml",
        "security/ir.model.access.csv",
        "views/hostel_room.xml",
        "views/hostel_register.xml",
        "views/hostel_staff.xml",
        "views/hostel_service.xml",
        "views/hostel_menus.xml",
    ],
}
