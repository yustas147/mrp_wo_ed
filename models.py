# -*- coding: utf-8 -*-

from openerp import models, fields, api


class mrp_production(models.Model):
    _name = 'mrp.production'
    _inherit = 'mrp.production'
    
    move_lines = fields.One2many('stock.move', 'raw_material_production_id', 'Products to Consume',
                                      domain=[('state', 'not in', ('done', 'cancel'))], readonly=False, states={'draft': [('readonly', False)]})
    move_created_ids = fields.One2many('stock.move', 'production_id', 'Products to Produce',
                                            domain=[('state', 'not in', ('done', 'cancel'))], readonly=False)
    move_created_ids2 = fields.One2many('stock.move', 'production_id', 'Produced Products',
                                         domain=[('state', 'in', ('done', 'cancel'))], readonly=False)


