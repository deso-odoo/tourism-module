# -*- coding: utf-8 -*-

from odoo import models, fields

class tourismCars(models.Model):
    _name = "tourism.cars"
    _description = "Cars Provided by Hotel"

    name = fields.Char(required=True)
    modelName = fields.Char(required=True)
    color = fields.Char(copy=False)
    description = fields.Text()
    available = fields.Boolean()
