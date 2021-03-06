# coding: utf-8
# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class PickingSummaryWizardProduct(models.TransientModel):
    _name = 'picking.summary.wizard.product'

    wizard_id = fields.Many2one(comodel_name='picking.summary.wizard')

    product_id = fields.Many2one(comodel_name='product.product')

    quantity_total = fields.Float()

    standard_price_total = fields.Float(
        compute='_compute_standard_price_total')

    @api.multi
    def _compute_standard_price_total(self):
        for line in self:
            line.standard_price_total =\
                line.product_id.standard_price * line.quantity_total
