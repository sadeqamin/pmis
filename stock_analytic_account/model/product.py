# -*- coding: utf-8 -*-
# Copyright 2014-17 Eficent Business and IT Consulting Services S.L.
# Copyright 2016 Matmoz d.o.o.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models
from odoo.tools.float_utils import float_round


class Product(models.Model):

    _inherit = "product.product"

    def _get_domain_locations(self):
        if self._context.get('analytic_account_id'):
            locations = self.env['stock.location'].search(
                [('analytic_account_id', '=', self._context.get(
                    'analytic_account_id'))]).ids
            dom_loc_out = dom_quant = [('location_id', '=', locations)]
            dom_loc_in = [('location_dest_id', '=', locations)]
            return (dom_quant, dom_loc_in, dom_loc_out)
        else:
            return super(Product, self)._get_domain_locations()
