# -*- coding: utf-8 -*-

from odoo import models, fields

class res_user(models.Model):
    _inherit = 'res.users'

    booking_ids = fields.One2many('tourism.bookings', 'name_id')
    