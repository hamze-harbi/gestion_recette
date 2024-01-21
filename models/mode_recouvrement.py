
from odoo import api, fields, models, _

class mode_recouvrement(models.Model):
    _name='mode.recouvrement'  
    _rec_name = 'code' 


    code = fields.Char(string="Code", tracking=True)
    libelle = fields.Char(string="Libelle", tracking=True)
    natureimpot_ids = fields.Many2many('nature.impot', string='Nature(s) d\'impôt')
    natureimpot_id = fields.Many2one('nature.impot', 'nature impôt', tracking=True)
 
 
  
    
    _sql_constraints = [('mode_recouv_uniq', 'unique(code)', 'Le nom du move de recouvrement doit être unique !')]
    
    