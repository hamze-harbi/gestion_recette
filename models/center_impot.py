
from odoo import api, fields, models, _

class center_impot(models.Model):
    _name='center.impot'
    _rec_name = 'code'

    code = fields.Char(string="Code", tracking=True)
    libelle = fields.Char(string="Libelle", tracking=True)
    natureimpot_ids = fields.Many2many('nature.impot', string='Nature')

    # _sql_constraints = [('centre_nom_uniq', 'unique(code)', 'Le nom de la centre doit être unique !')]
    