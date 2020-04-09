# -*- coding: utf-8 -*-
from odoo import http

# class StockAvaliableQty(http.Controller):
#     @http.route('/stock_avaliable_qty/stock_avaliable_qty/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stock_avaliable_qty/stock_avaliable_qty/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('stock_avaliable_qty.listing', {
#             'root': '/stock_avaliable_qty/stock_avaliable_qty',
#             'objects': http.request.env['stock_avaliable_qty.stock_avaliable_qty'].search([]),
#         })

#     @http.route('/stock_avaliable_qty/stock_avaliable_qty/objects/<model("stock_avaliable_qty.stock_avaliable_qty"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stock_avaliable_qty.object', {
#             'object': obj
#         })