from odoo import api, fields, models


class Member(models.Model):
    _inherit = 'res.partner'
    _description = 'Newscription'

    level = fields.Selection([
        ('platinum', 'Platinum'),
        ('gold', 'Gold'),
        ('silver', 'Silver'),
        ('normal', 'Normal'),
    ], string='Level')
    
