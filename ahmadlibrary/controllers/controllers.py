# -*- coding: utf-8 -*-
# from odoo import http


# class Ahmadlibrary(http.Controller):
#     @http.route('/ahmadlibrary/ahmadlibrary', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ahmadlibrary/ahmadlibrary/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ahmadlibrary.listing', {
#             'root': '/ahmadlibrary/ahmadlibrary',
#             'objects': http.request.env['ahmadlibrary.ahmadlibrary'].search([]),
#         })

#     @http.route('/ahmadlibrary/ahmadlibrary/objects/<model("ahmadlibrary.ahmadlibrary"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ahmadlibrary.object', {
#             'object': obj
#         })
