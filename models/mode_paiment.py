from odoo import api, fields, models, _

class mode_paiement(models.Model):
    _name='mode.paiement' 
    _inherit = ['mail.thread','mail.activity.mixin']   
    _rec_name = 'name'

    name = fields.Char(string="Nom", tracking=True)
    
    libelle = fields.Char(string="Libelle", tracking=True)
    
    _sql_constraints = [('modepaiement_type_uniq', 'unique(name)', 'Le nom du mode paiement doit être unique !')]
    
    