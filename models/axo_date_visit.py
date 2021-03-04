# -*- coding: utf-8 -*-

from odoo import models, fields, api

class axo_date_visit(models.Model):
    _name = "axo.date.visit"

    name = fields.Char(
         string="Name", 
         required=True)
    
    day = fields.Selection(
        selection= [
            ("mon","Monday"),
            ("tue","Tuesday"),
            ("web","Wednesday"),
            ("Thu","Thursday"),
            ("fri","Friday"),
            ("Sat","Saturday"),
            ("sun","Sunday")],string="Days",required=True )

    time = fields.Float(
        string="Hours" ,
        required = True )
    # agrega en views <field name='time' widget='float_time' />




