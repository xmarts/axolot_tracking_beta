# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AxoZone(models.Model):
     _name = "axo.zone"
     _description = 'Zona que tendrá acción para el reparto o entrega'

     name = fields.Char(
          string="name",
          required=True,)

     user_id = fields.Many2one("hr.employee", string="empleado", readonly=False, index=True ) 
 
     type = fields.Selection(
          selection=[
               ("sales","Sales"),
               ("presales","PreSales"),
               ("delivery","Delivery"),
               ("service","Service")
          ],
          string="sale type" , required=True )
