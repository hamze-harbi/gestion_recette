
{
    "name": "Gestion de Recettes",
    "summary": "Gestion de Recettes",
    "author": "HATECH",
    "website": "www.hornafricatech.com",
    "category": "Custom Application",
    "version": "2.0",
    "license": "AGPL-3",
    "depends": ['base','mail'],
    "data": [
        #'data/courrier_data.xml',
        'data/sequence.xml',
        'views/main_menu_file_view.xml',       
        'views/recouvrement_declaration.xml',
        'views/recouvrement_analyse.xml',
        'views/center_impot.xml',
        'views/mode_recouvrement.xml',
        'views/banque.xml',
        'views/mode_paiement.xml',
        'views/ligne_declaration.xml',
        'views/nature_impot.xml',
   #     'security/ir.model.access.csv',

   #     'views/whatsapp_template.xml',
 #       'views/wizard.xml',
  #      'views/sms_template.xml',
        

        ],
    "application": True,
    "development_status": "Beta",
    "maintainers": ["Horn Africa Technology"],
}
