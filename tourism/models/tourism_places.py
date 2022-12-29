# -*- coding: utf-8 -*-

from odoo import models, fields

class tourismPlaces(models.Model):
    _name = "tourism.places"
    _description = "Consists of all Tourism places available"

    name = fields.Char()
    country = fields.Char()
    description = fields.Text()
    duration = fields.Integer()
    price = fields.Float()
    including_flights = fields.Boolean()
    hotel_id = fields.Many2one('tourism.hotels', string="Hotel")
    activities_ids = fields.Many2many('tourism.activities', string="Actvities")
