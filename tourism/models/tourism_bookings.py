# -*- coding: utf-8 -*-

from odoo import models, fields, api

class tourismBookings(models.Model):
    _name = "tourism.bookings"
    _description = "Booking related data"

    name_id = fields.Many2one('res.users', string="Booked By", required=True)
    place_id = fields.Many2one('tourism.places', string="Places", required=True)
    book_seats = fields.Integer(required=True)
    total_price = fields.Integer(compute="_compute_total_price")

    @api.depends('book_seats', 'place_id.price')
    def _compute_total_price(self):
        for record in self:
            record.total_price = record.book_seats * record.place_id.price
