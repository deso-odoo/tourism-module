# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TourismPlaces(models.Model):
    _name = "tourism.places"
    _description = "Consists of all Tourism places available"
    _order = "id desc"

    name = fields.Char()
    country_id = fields.Many2one('res.country', string="Country")
    description = fields.Text()
    duration = fields.Integer()
    price = fields.Float()
    # total_seats = fields.Integer()
    # available_seats = fields.Integer(compute="_compute_available_seats")
    including_flights = fields.Boolean()
    flight_price = fields.Integer()
    including_road = fields.Boolean()
    road_price = fields.Integer()
    including_rail = fields.Boolean()
    train_price = fields.Integer()
    state = fields.Selection(
        selection=[('a_new', 'New'), ('b_bookings_open', 'Bookings Open'), ('c_bookings_closed', 'Bookings Closed'), ('d_cancel', 'Cancel')],
        default='a_new'
    )
    user_id = fields.Many2one('res.users', default=lambda self: self.env.user)

    # hotel_id
    # hotel_id = fields.Many2one("tourism.hotels", string="Hotel")

    # mode_of_transportation = fields.Selection(
        # selection=[('road', 'Road'), ()]
    # )
    hotel_id = fields.Many2one('tourism.hotels', domain="[('hotel_country_id', '=', country_id)]")
    hotel_price = fields.Integer(related='hotel_id.hotel_price')
    activities_ids = fields.Many2many('tourism.activities','place_activities_rel','activity_id', 'place_id', string="Actvities")
    booking_ids = fields.One2many('tourism.bookings', 'place_id')
    total_booked_seats = fields.Integer(compute="_compute_booked_seats", default=0)
    # booked_id = fields.Many2one('res.user')
    image = fields.Binary(attachment=True, store=True)

    _sql_constraints = [
        ('check_price', 'CHECK(price>=0)', 'The Price must be Positive!!!'),
        ('check_duration', 'CHECK(duration>=0)', 'The Duration must be Positive!!!'),
        # ('check_seats', 'CHECK(total_seats>=0)', 'Total Seats must be Positive!!!')
    ]

    # @api.depends('total_seats','total_booked_seats')
    # def _compute_available_seats(self):
    #     for record in self:
    #         # if record.total_booked_seats < record.total_seats:
    #         record.available_seats = record.total_seats - record.total_booked_seats

    # @api.depends('booking_ids.book_seats')
    def _compute_booked_seats(self):
        for record in self:
            record.total_booked_seats = sum(record.booking_ids.mapped('book_seats'))

    # Actions
    def action_start_booking(self):
        for record in self:
            record.state = 'b_bookings_open'
        return True

    def action_cancel(self):
        for record in self:
            record.state = 'd_cancel'
        return True

    def action_close_booking(self):
        for record in self:
            record.state = 'c_bookings_closed'
        return True
    # @api.constrains('available_seats')
    # def _check_available_seats(self):
    #     for record in self:
    #         if (record.total_booked_seats > record.total_seats):
    #             raise ValidationError('Seats not available!!!')

