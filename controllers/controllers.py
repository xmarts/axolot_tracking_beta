# -*- coding: utf-8 -*-
# from odoo import http


# class MyModule4(http.Controller):
#     @http.route('/my_module4/my_module4/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_module4/my_module4/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_module4.listing', {
#             'root': '/my_module4/my_module4',
#             'objects': http.request.env['my_module4.my_module4'].search([]),
#         })

#     @http.route('/my_module4/my_module4/objects/<model("my_module4.my_module4"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_module4.object', {
#             'object': obj
#         })
