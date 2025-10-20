from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    auto_bom_in_pos = fields.Boolean(
        string="Déduire automatiquement la BOM en POS",
        help="Si activé, un ordre de fabrication sera automatiquement créé et validé "
             "lorsque ce produit est vendu dans le POS."
    )
