from odoo import api, fields, models, _

class ligne_declaration(models.Model):
    _name='ligne.declaration'   
    _inherit = ['mail.thread','mail.activity.mixin'] 
    _rec_name = 'refligne'

    refligne = fields.Char('Ref')
    centre_id = fields.Many2one('center.impot','Centre impôt',
                                default=lambda self: self._default_center_impot())
    nature_id = fields.Many2one('nature.impot','Nature impôt')
    moderecouvrement_id = fields.Many2one('mode.recouvrement', 'Mode recouvrement')
    banque_id = fields.Many2one('res.bank', 'Banque')
    modepaiement_id = fields.Many2one('mode.paiement', 'Mode paiement')
    montant = fields.Float(string="Montant")
    modepaiement_name = fields.Char(related='modepaiement_id.name', store=True)

    declaration_id = fields.Many2one(
        'recouvrement.declaration',
        string='Declaration',
        ondelete='cascade',
    )

    @api.model
    def _default_center_impot(self):
        # Get the center.impot assigned to the current user
        current_user = self.env.user
        # assigned_center_impot = self.env['center.impot'].search([(' natureimpot_id', 'in', [current_user.id])], limit=1)

        #  Return the assigned center.impot or False if not found
        # return assigned_center_impot.id if assigned_center_impot else False    

    @api.onchange('modepaiement_id')
    def onchange_modepaiement_id(self):
        if self.modepaiement_name != 'CH':
            self.banque_id = False

    @api.onchange('centre_id')
    def onchange_centre(self):
        return {'domain': {'nature_id': [('centreimpot_id', '=', self.centre_id.id)]}}
    
    
    
    
    
    
    
    # @api.onchange('modepaiement_id')
    # def onchange_payement_methode(self):
    #     if self.modepaiement_id.name == 'CH':
    #         # If modepaiement_id is 'CH', make the banque_id field visible
    #         return {'domain': {'banque_id': [('id', '!=', False)]}}
    #     else:
    #         # If modepaiement_id is not 'CH', make the banque_id field invisible
    #         return {'value': {'banque_id': False}}

   
    

