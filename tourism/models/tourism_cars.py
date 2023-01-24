# -*- coding: utf-8 -*-

from odoo import models, fields

class TourismCars(models.Model):
    _name = "tourism.cars"
    _description = "Cars Provided by Hotel"

    name = fields.Char(required=True)
    modelName = fields.Char(required=True)
    Color = fields.Integer(copy=False)
    description = fields.Text()
    available = fields.Boolean()
