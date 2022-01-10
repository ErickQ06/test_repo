# -*- coding: utf-8 -*-
# from odoo import http


# class TestRepo(http.Controller):
#     @http.route('/test_repo/test_repo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_repo/test_repo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_repo.listing', {
#             'root': '/test_repo/test_repo',
#             'objects': http.request.env['test_repo.test_repo'].search([]),
#         })

#     @http.route('/test_repo/test_repo/objects/<model("test_repo.test_repo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_repo.object', {
#             'object': obj
#         })
