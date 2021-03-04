# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AxoTrackingType(models.Model):
    _name = "axo.tracking.type"

    name = fields.Char(string="name", required=True)