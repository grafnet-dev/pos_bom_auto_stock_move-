from odoo import models, api


class PosOrder(models.Model):
    _inherit = 'pos.order'

    @api.model
    def action_pos_order_paid(self):
        res = super().action_pos_order_paid()

        for order in self:
            for line in order.lines:
                product = line.product_id
                qty = line.qty

                # 🔹 Vérifie si le produit est configuré pour déduire la BOM
                if not product.product_tmpl_id.auto_bom_in_pos:
                    continue

                # 🔹 Cherche une BOM pour ce produit
                bom = self.env['mrp.bom']._bom_find(product=product)
                if not bom:
                    continue

                mo = self.env['mrp.production'].create({
                    'product_id': product.id,
                    'product_qty': qty,
                    'product_uom_id': product.uom_id.id,
                    'bom_id': bom.id,
                    'location_src_id': self.env.ref('stock.stock_location_stock').id,
                    'location_dest_id': self.env.ref('stock.stock_location_stock').id,
                    'origin': f"POS Order {order.name}",
                })

                mo.action_confirm()
                mo.action_assign()
                mo.action_mark_done()
                
                _logger = self.env['ir.logging']
                _logger.create({
                    'name': 'POS Auto MO',
                    'type': 'server',
                    'dbname': self.env.cr.dbname,
                    'level': 'info',
                    'message': f"MO créé automatiquement pour {product.display_name} ({qty}) dans {order.name}",
                    'path': __name__,
                    'line': 0,
                    'func': 'action_pos_order_paid',
                })

        return res
