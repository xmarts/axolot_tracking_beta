# -*- coding: utf-8 -*-

from odoo import models, fields, api

class axo_route_order(models.Model):
  _name = "axo.route.order"
    
  name = fields.Char(string="Name",required=True)#falta el search

  partner_id = fields.Many2one("res.partner",auto_join=True,track_visibility="onchange")
 

  partner_shipping_id = fields.Many2one("partner_id", string="address", required= True)

  priority = fields.Selection(
    selection=[
          ("C","Critica"),
          ("A","Alta"),
          ("N","Normal"),
          ("B","Baja")
        ],
    string="Priority" , required=True )
        # widget (Priority)

  partner_mail = fields.Char(
    string="Mail",
    related="partner_id.email")

  partner_phone = fields.Char(
    string="Phone",
    related="partner_id.phone")

  employee_id = fields.Many2one("hr.employee",string="Assigned to",readonly=False,index=True)

  planened_date_begin = fields.Datetime(store=True)#widget daterange

  planned_date_real = fields.Datetime(store=True,related="planened_date_begin")  #widget daterange related camp

  tracking_tag_id = fields.Many2many("axo.tracking.tag") #widget many2many_tag
    
  type_id = fields.Many2one("axo.tracking.type",string="Selection") # widget status bar

  stage = fields.Selection(
    selection=[
      ("0","Sin Sincronizar"),
      ("1","Sin Descargar"),
      ("2","Pendiente"),
      ("3","Incompleta"),
      ("4","Completa"),
      ("6","Cerrado"),
      ("11","Error")
      ],
    string="Stage")

  
  exception_id = fields.Many2one("axo.exception",string="Exception")
  
  # este tipo es un turista
  request_date = fields.Date(default=lambda s: fields.Date.today())
 
  # este es otro turista
  google_map_partner = fields.Char(string="map")
  
class Partner(models.Model):
  _name = "partner"
  inherit ="res.partner"
    
  zone = fields.Many2many("axo.date.visit", "day", string="Zone")
    
  zone2 = fields.Many2many("axo.date.visit", "day2", string="Zone 2")
    
  zone3 = fields.Many2many("axo.date.visit", "day3", string="Zone 3")
    
  zone4 = fields.Many2many("axo.date.visit", "day4", string="Zone 4")

 # new_route = fields.Many2many("axo.zone", "axo.tracking.type", "day", "Partner.id",string="New Route")