from odoo import models, fields

class Banque(models.Model):
    _inherit = 'res.bank'
    _name = 'banque' 
    field_name = fields.Char(string='Field Label')
  
