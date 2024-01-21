from odoo import api, fields, models, _

class recouvrement_declaration(models.Model):
    _name = "recouv.declaration"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Gestion de Recette"

    #refcourrier = fields.Char(string="Référence courrier" ,required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    # refcourrier = fields.Char(string="Référence courrier" )
    contribuable_id = fields.Many2one('res.partner', 'Contribuable', tracking=True,  size=32)

    quittance = fields.Char(string="Numéro Quittance")
    note = fields.Char(string="Note")
    date_declaration = fields.Datetime(string="Date Déclaration")
    montant_total = fields.Float(string="Montant total", compute='_compute_montant_total', store=True)

    ligne_declaration_ids = fields.One2many(
        'ligne.declaration',
        'declaration_id',
        string='Ligne Declarations',
        copy=True,  # Set copy=True to allow copying the lines when duplicating the declaration record
         editable=True,
    )

    
    
    # @api.model
    # def create(self, vals):
    #     seq = self.env["ir.sequence"].next_by_code("suivi.courrier.seq") or 0
    #     vals["refcourrier"] = seq
    #     print("************************************************* newwwwwwww *********************************", vals["refcourrier"])
    #     return super().create(vals)
    
    @api.depends('ligne_declaration_ids.montant')
    def _compute_montant_total(self):
        for declaration in self:
            montant_total = sum(declaration.ligne_declaration_ids.mapped('montant'))
            declaration.montant_total = montant_total

# class courrier_config(models.Model):
#     _name='courrier.config'    


#     url = fields.Char(string="url API")
#     id_repertoire = fields.Char(string="ID Répertoire")
#     id_modele = fields.Char(string="ID Modèle")
#     convidenciality = fields.Char(string="Confidentialité")
#     utilisateur = fields.Char('Utilisateur')
