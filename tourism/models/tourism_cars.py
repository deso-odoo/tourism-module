# -*- coding: utf-8 -*-

from odoo import models, fields

class tourismCars(models.Model):
    _name = "tourism.cars"
    _description = "Cars Provided by Hotel"

    name = fields.Char()
    modelName = fields.Char()
    color = fields.Char()
    description = fields.Text()
    available = fields.Boolean()
