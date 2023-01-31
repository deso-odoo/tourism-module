# -*- coding: utf-8 -*-

from odoo import models, fields, api

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
    booking_ids = fields.One2many('tourism.bookings', 'hotel_id')
    booking_count = fields.Integer(compute="_compute_booking_count", string="Booking Count")
    user_id = fields.Many2one('res.users', default=lambda self: self.env.user)
    
    # Compute Methods
    @api.depends('booking_ids')
    def _compute_booking_count(self):
        for record in self:
            record.booking_count = len(record.booking_ids)