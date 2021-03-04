# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Axo_Exception(models.Model):
    _name = "axo.exception"

    cod = fields.Char(string="code",required=True)
    exception_char = fields.Char(string="Exception", required=True)
     


