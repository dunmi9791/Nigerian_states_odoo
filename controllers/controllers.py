# -*- coding: utf-8 -*-
# from odoo import http


# class NigStates(http.Controller):
#     @http.route('/nig_states/nig_states', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nig_states/nig_states/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('nig_states.listing', {
#             'root': '/nig_states/nig_states',
#             'objects': http.request.env['nig_states.nig_states'].search([]),
#         })

#     @http.route('/nig_states/nig_states/objects/<model("nig_states.nig_states"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nig_states.object', {
#             'object': obj
#         })
