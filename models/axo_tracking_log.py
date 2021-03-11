# -*- coding: utf-8 -*-

from odoo import models, fields, api

class axo_tracking_log(models.Model):
  _name = "axo.tracking.log"

  datetime_c = fields.Datetime()
     
#geo falta 
          
  user_id = fields.Many2one("hr.employee",string= "empleado",readonly=False,index=True)

  route_order_id = fields.Many2one("project.task",string="Route Order")

class trackingemployee(models.Model):
  _name = "tr.employee"
  inherit = "hr.employee"
  password = fields.Char(string="Password")
     
  rol_type = fields.Many2one("axo.rol.type",string="Rol")
    
  tracking_hours = fields.Many2one("resource.calendar",string="Tracking Hour")
     
  monitoring = fields.Integer(default=10,string="Time Monitoring")