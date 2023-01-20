# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class tourismBookings(models.Model):
    _name = "tourism.bookings"
    _description = "Booking related data"

    name_id = fields.Many2one('res.users', string="Booked By", required=True)
    place_id = fields.Many2one('tourism.places', string="Places", required=True)
    book_seats = fields.Integer(required=True)
    tax = fields.Integer(compute="_compute_tax")
    total_price = fields.Integer(compute="_compute_total_price")

    @api.depends('book_seats', 'place_id.price')
    def _compute_tax(self):
        for record in self:
            record.tax = (record.book_seats*record.place_id.price) * 0.18

    @api.depends('book_seats', 'place_id.price', 'place_id.hotel_price')
    def _compute_total_price(self):
        for record in self:
            record.total_price = ((record.place_id.price + record.place_id.hotel_price) * record.book_seats) + record.tax
            # record.total_price = record.book_seats * record.place_id.price + record.tax
    
    @api.constrains('book_seats')
    def _check_booking_numbers(self):
        for record in self:
            if record.place_id.available_seats < record.book_seats:
                raise ValidationError("Seats not available")
