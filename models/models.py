# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class pos_bom_auto_stock_move(models.Model):
#     _name = 'pos_bom_auto_stock_move.pos_bom_auto_stock_move'
#     _description = 'pos_bom_auto_stock_move.pos_bom_auto_stock_move'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

