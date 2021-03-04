# -*- coding: utf-8 -*-

from odoo import models, fields, api

class axo_tracking_tag(models.Model):
    _name = "axo.tracking.tag"
    _description = " tracking tag"

    name = fields.Char(
        string="name",
        required=True)

    color = fields.Char(string = "color")

