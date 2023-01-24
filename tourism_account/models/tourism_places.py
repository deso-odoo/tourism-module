# -*- coding: utf-8 -*-

from odoo import models, fields, Command

class TourismPlaces(models.Model):
    _inherit = 'tourism.bookings'

    def action_confirm_booking(self):
        for record in self:
            self.env['account.move'].create({
                'partner_id': record.name_id.id,
                'move_type': 'out_invoice',
                'invoice_line_ids':[
                    Command.create({
                        'name': self.name_id.name,
                        'quantity': record.book_seats,
                        'price_unit': record.total_price
                    })
                ]
            })
        return super(TourismPlaces, self).action_confirm_booking()
