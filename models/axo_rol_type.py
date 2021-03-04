# -*- coding: utf-8 -*-

from odoo import models, fields, api

class axo_rol_type(models.Model):
     _name = "axo.rol.type"

     cod = fields.Char(string="Code",required =True)
     name = fields.Char(string="Name", required=True)
