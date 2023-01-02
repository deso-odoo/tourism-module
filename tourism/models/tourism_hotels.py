# -*- coding: utf-8 -*-

from odoo import models, fields

class tourismHotel(models.Model):
    _name="tourism.hotels"
    _description = "list of hotels"

    name=fields.Char(required=True)
    city=fields.Char(required=True)
    description = fields.Text()
    availablility = fields.Boolean()
    address = fields.Text(required=True)
    required_days = fields.Integer()
    cars_ids = fields.Many2many('tourism.cars', string="Cars")
