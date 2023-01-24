# -*- coding: utf-8 -*-

from odoo import models, fields

class ResUser(models.Model):
    _inherit = 'res.users'

    booking_ids = fields.One2many('tourism.bookings', 'name_id')
    