# -*- coding: utf-8 -*-

from odoo import models, fields

class tourismActivities(models.Model):
    _name = "tourism.activities"
    _description = "Includes the list of activities during a tour"

    name = fields.Char(required = True)
