{
    'name': 'POS BOM Auto Manufacturing',
    'version': '1.0',
    'summary': 'Crée automatiquement un ordre de fabrication lors de la vente POS d’un produit avec nomenclature',
    'author': 'TonNom / TonEntreprise',
    'category': 'Point of Sale',
    'depends': ['point_of_sale', 'mrp', 'stock', 'product'],
    'data': [
        'views/product_template_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
