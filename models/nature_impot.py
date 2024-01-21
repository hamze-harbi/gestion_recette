
from odoo import api, fields, models, _

class nature_impot(models.Model):
    _name='nature.impot'    
    _rec_name = 'libelle'

    code = fields.Char(string="Code", tracking=True)
    libelle = fields.Char(string="Libelle", tracking=True)
    centreimpot_id = fields.Many2one('center.impot', 'Centre impôt', tracking=True)
    moderecouvrement_id = fields.Many2many('mode.recouvrement', string='Mode')
    
    
    
    

     
    
    
    
    # _sql_constraints = [('nature_impot_uniq', 'unique(code)', 'Le nom du Nature impot doit être unique !')]
    
    
