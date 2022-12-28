# -*- coding: utf-8 -*-

from odoo import models, fields

class tourismHotel(models.Model):
    _name="tourism.hotels"
    _description = "list of hotels"

    name=fields.Char()
    description = fields.Text()
    availablility = fields.Boolean()
    address = fields.Text()
    required_days = fields.Integer()