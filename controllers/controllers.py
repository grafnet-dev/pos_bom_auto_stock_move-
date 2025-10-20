# -*- coding: utf-8 -*-
# from odoo import http


# class PosBomAutoStockMove(http.Controller):
#     @http.route('/pos_bom_auto_stock_move/pos_bom_auto_stock_move', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_bom_auto_stock_move/pos_bom_auto_stock_move/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_bom_auto_stock_move.listing', {
#             'root': '/pos_bom_auto_stock_move/pos_bom_auto_stock_move',
#             'objects': http.request.env['pos_bom_auto_stock_move.pos_bom_auto_stock_move'].search([]),
#         })

#     @http.route('/pos_bom_auto_stock_move/pos_bom_auto_stock_move/objects/<model("pos_bom_auto_stock_move.pos_bom_auto_stock_move"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_bom_auto_stock_move.object', {
#             'object': obj
#         })

