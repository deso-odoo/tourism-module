# -*- coding: utf-8 -*-

from odoo import models, fields

class TourismHotel(models.Model):
    _name="tourism.hotels"
    _description = "list of hotels"

    name=fields.Char(required=True)
    hotel_country_id=fields.Many2one('res.country')
    description = fields.Text()
    availablility = fields.Boolean()
    address = fields.Text(required=True)
    required_days = fields.Integer()
    cars_ids = fields.Many2many('tourism.cars', string="Cars")
    # place_id = fields.Many2one('tourism.places')
    sequence = fields.Integer(default=1)
    hotel_price = fields.Integer()