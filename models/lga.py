# -*- coding: utf-8 -*-

from odoo import models, fields, api


class lga(models.Model):
    _name = 'state.lga'
    _description = 'lga'

    name = fields.Char(string='Name', required=True)
    state_id = fields.Many2one(
        comodel_name='res.country.state',
        string='State',
        required=True)


class ResPartner(models.Model):

    _inherit = 'res.partner'

    lga = fields.Many2one(
        comodel_name='state.lga',
        string='Lga',
        required=False)
