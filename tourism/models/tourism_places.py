# -*- coding: utf-8 -*-

from odoo import models, fields, api

class tourismPlaces(models.Model):
    _name = "tourism.places"
    _description = "Consists of all Tourism places available"

    name = fields.Char()
    country_id = fields.Many2one('res.country', string="Country")
    description = fields.Text()
    duration = fields.Integer()
    price = fields.Float()
    total_seats = fields.Integer()
    available_seats = fields.Integer(compute="_compute_available_seats")
    including_flights = fields.Boolean()
    state = fields.Selection(
        selection=[('new', 'New'), ('bookings_open', 'Bookings Open'), ('full', 'Bookings Full'), ('cancel', 'Cancel')],
        default='new'
    )
    # hotels_id = fields.Many2one('tourism.hotels')
    # hotel_id = fields.Many2one('tourism.hotels', string="Hotel", domain="[('place_id.country_id','=','hotel_country_id')]")
    hotel_id = fields.Many2one('tourism.hotels', string="Hotel")
    activities_ids = fields.Many2many('tourism.activities','place_activities_rel','activity_id', 'place_id', string="Actvities")
    booking_ids = fields.One2many('tourism.bookings', 'place_id')
    total_booked_seats = fields.Integer(compute="_compute_booked_seats", default=0)

    _sql_constraints = [
        ('check_price', 'CHECK(price>=0)', 'The Price must be Positive!!!'),
        ('check_duration', 'CHECK(duration>=0)', 'The Duration must be Positive!!!'),
        ('check_seats', 'CHECK(total_seats>=0)', 'Total Seats must be Positive!!!')
    ]

    @api.depends('total_seats','total_booked_seats')
    def _compute_available_seats(self):
        for record in self:
            record.available_seats = record.total_seats - record.total_booked_seats

    @api.depends('booking_ids.book_seats')
    def _compute_booked_seats(self):
        for record in self:
            record.total_booked_seats = sum(record.booking_ids.mapped('book_seats'))

    # Actions
    def action_start_booking(self):
        for record in self:
            record.state = 'bookings_open'
        return True

    def action_cancel(self):
        for record in self:
            record.state = 'cancel'
        return True