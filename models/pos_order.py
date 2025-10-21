from odoo import models, api
import logging

_logger = logging.getLogger(__name__)

class PosOrder(models.Model):
    _inherit = 'pos.order'

    @api.model
    def action_pos_order_paid(self):
        _logger.info("=== [POS BOM AUTO] action_pos_order_paid déclenchée ===")
        res = super().action_pos_order_paid()

        for order in self:
            _logger.info(f"[POS BOM AUTO] ➡️ Traitement de la commande {order.name} (ID: {order.id})")

            for line in order.lines:
                product = line.product_id
                qty = line.qty
                _logger.info(f"   → Ligne : {product.display_name} (qty={qty})")

                # Vérifie si le produit est configuré pour déduire la BOM
                if not product.product_tmpl_id.auto_bom_in_pos:
                    _logger.info(f"      ❌ Produit {product.display_name} sans option auto_bom_in_pos, on saute.")
                    continue

                # Recherche de la BOM
                bom = self.env['mrp.bom'].search([
                    '|',
                    ('product_id', '=', product.id),
                    '&',
                    ('product_id', '=', False),
                    ('product_tmpl_id', '=', product.product_tmpl_id.id),
                    ('company_id', 'in', [order.company_id.id, False]),
                ], limit=1)

                if not bom:
                    _logger.warning(f"      ⚠️ Aucune BOM trouvée pour {product.display_name}")
                    continue

                _logger.info(f"      ✅ BOM trouvée ({bom.display_name}) → Déduction du stock des composants...")

                # Récupère entrepôt
                warehouse = self.env['stock.warehouse'].search([('company_id', '=', order.company_id.id)], limit=1)
                if not warehouse:
                    _logger.error(f"      🚫 Aucun entrepôt trouvé pour la société {order.company_id.name}")
                    continue
                _logger.info(f"      🏢 Entrepôt utilisé : {warehouse.name}")

                # Récupère emplacement source (stock)
                location_stock = warehouse.lot_stock_id
                if not location_stock:
                    _logger.error(f"      🚫 Emplacement de stock principal introuvable pour {warehouse.name}")
                    continue
                _logger.info(f"      📦 Emplacement source : {location_stock.complete_name}")

                # Emplacement de destination
                location_dest = self.env['stock.location'].search([
                    ('complete_name', '=', 'RC/Consommations POS')
                ], limit=1)
                if not location_dest:
                    _logger.warning("      ⚠️ Emplacement 'RC/Consommations POS' introuvable, utilisation du 'Scrap'")
                    location_dest = self.env.ref('stock.stock_location_scrapped')
                _logger.info(f"      🎯 Emplacement destination : {location_dest.complete_name}")

                # Type de picking
                picking_type = self.env['stock.picking.type'].search([
                    ('code', '=', 'internal'),
                    ('warehouse_id', '=', warehouse.id)
                ], limit=1)
                if not picking_type:
                    _logger.warning("      ⚠️ Aucun type de picking 'internal' trouvé → mouvement créé sans picking_type")
                else:
                    _logger.info(f"      🚚 Type d'opération : {picking_type.display_name}")

                # Parcours des composants de la BOM
                for bom_line in bom.bom_line_ids:
                    component = bom_line.product_id
                    component_qty = bom_line.product_qty * qty

                    _logger.info(f"         🔹 Composant : {component.display_name} (x{component_qty})")

                    # Vérifie le type de produit
                    # Vérifie si le composant est stockable selon le modèle Odoo 18
                    if component.type != 'consu' or not component.is_storable:
                        _logger.warning(
                            f"⚠️ Composant {component.display_name} n'est pas stockable "
                            f"(type={component.type}, is_storable={component.is_storable}) → pas de déduction."
                        )
                        continue


                    from odoo import models, api
import logging

_logger = logging.getLogger(__name__)

class PosOrder(models.Model):
    _inherit = 'pos.order'

    @api.model
    def action_pos_order_paid(self):
        _logger.info("=== [POS BOM AUTO] action_pos_order_paid déclenchée ===")
        res = super().action_pos_order_paid()

        for order in self:
            _logger.info(f"[POS BOM AUTO] ➡️ Traitement de la commande {order.name} (ID: {order.id})")

            for line in order.lines:
                product = line.product_id
                qty = line.qty
                _logger.info(f"   → Ligne : {product.display_name} (qty={qty})")

                # Vérifie si le produit est configuré pour déduire la BOM
                if not product.product_tmpl_id.auto_bom_in_pos:
                    _logger.info(f"      ❌ Produit {product.display_name} sans option auto_bom_in_pos, on saute.")
                    continue

                # Recherche de la BOM
                bom = self.env['mrp.bom'].search([
                    '|',
                    ('product_id', '=', product.id),
                    '&',
                    ('product_id', '=', False),
                    ('product_tmpl_id', '=', product.product_tmpl_id.id),
                    ('company_id', 'in', [order.company_id.id, False]),
                ], limit=1)

                if not bom:
                    _logger.warning(f"      ⚠️ Aucune BOM trouvée pour {product.display_name}")
                    continue

                _logger.info(f"      ✅ BOM trouvée ({bom.display_name}) → Déduction du stock des composants...")

                # Récupère entrepôt
                warehouse = self.env['stock.warehouse'].search([('company_id', '=', order.company_id.id)], limit=1)
                if not warehouse:
                    _logger.error(f"      🚫 Aucun entrepôt trouvé pour la société {order.company_id.name}")
                    continue
                _logger.info(f"      🏢 Entrepôt utilisé : {warehouse.name}")

                # Récupère emplacement source (stock)
                location_stock = warehouse.lot_stock_id
                if not location_stock:
                    _logger.error(f"      🚫 Emplacement de stock principal introuvable pour {warehouse.name}")
                    continue
                _logger.info(f"      📦 Emplacement source : {location_stock.complete_name}")

                # Emplacement de destination
                location_dest = self.env['stock.location'].search([
                    ('complete_name', '=', 'RC/Consommations POS')
                ], limit=1)
                if not location_dest:
                    _logger.warning("      ⚠️ Emplacement 'RC/Consommations POS' introuvable, utilisation du 'Scrap'")
                    location_dest = self.env.ref('stock.stock_location_scrapped')
                _logger.info(f"      🎯 Emplacement destination : {location_dest.complete_name}")

                # Type de picking
                picking_type = self.env['stock.picking.type'].search([
                    ('code', '=', 'internal'),
                    ('warehouse_id', '=', warehouse.id)
                ], limit=1)
                if not picking_type:
                    _logger.warning("      ⚠️ Aucun type de picking 'internal' trouvé → mouvement créé sans picking_type")
                else:
                    _logger.info(f"      🚚 Type d'opération : {picking_type.display_name}")

                # Parcours des composants de la BOM
                for bom_line in bom.bom_line_ids:
                    component = bom_line.product_id
                    component_qty = bom_line.product_qty * qty

                    _logger.info(f"         🔹 Composant : {component.display_name} (x{component_qty})")

                    # Vérifie le type de produit
                    # Vérifie si le composant est stockable selon le modèle Odoo 18
                    if component.type != 'consu' or not component.is_storable:
                        _logger.warning(
                            f"⚠️ Composant {component.display_name} n'est pas stockable "
                            f"(type={component.type}, is_storable={component.is_storable}) → pas de déduction."
                        )
                        continue


                    move_vals = {
                        'name': f"POS Auto BOM ({order.name}) - {product.display_name}",
                        'product_id': component.id,
                        'product_uom_qty': component_qty,
                        'product_uom': component.uom_id.id,
                        'location_id': location_stock.id,
                        'location_dest_id': location_dest.id,
                        'origin': f"POS Order {order.name}",
                        'company_id': order.company_id.id,
                        'picking_type_id': picking_type.id if picking_type else False,
                    }

                    move = self.env['stock.move'].create(move_vals)
                    _logger.info(f"         ✅ Mouvement créé (ID: {move.id}) pour {component.display_name}")

                    try:
                        move._action_confirm()
                        _logger.info(f"         ⚙️  move._action_confirm() OK (state={move.state})")

                        move._action_assign()
                        _logger.info(f"         ⚙️  move._action_assign() OK (state={move.state})")

                        move._action_done()
                        _logger.info(f"         🟢 move._action_done() OK (state={move.state})")

                    except Exception as e:
                        _logger.error(f"         ❌ Erreur pendant l'exécution du mouvement : {e}")

                    # Vérifie le résultat
                    _logger.info(f"         📊 Résumé du move: produit={component.display_name}, état={move.state}, qty={move.product_uom_qty}, loc_from={move.location_id.complete_name}, loc_to={move.location_dest_id.complete_name}")

        _logger.info("=== [POS BOM AUTO] Fin de action_pos_order_paid ===")
        return res

