{
    'name': 'Confirm Before Save',
    'version': '17.0.1.0.0',
    'category': 'Tools',
    'summary': 'Prevent accidental auto-save with confirmation dialogs',
    'description': """
        Confirm Before Save
        ===================
        This module solves the common problem of accidental data changes in Odoo by:
        
        * Adding confirmation dialogs when navigating away with unsaved changes
        * Providing visual indicators for modified records
        * Allowing per-model configuration of save confirmation
        * Giving administrators control over the feature per company
        
        Features:
        ---------
        * Visual indicator when form data is modified
        * Confirmation dialog before auto-save on navigation
        * Settings to enable/disable per model
        * User-friendly interface
        * Works with all standard Odoo forms
    """,
    'author': 'Mohamed Anwar',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_config_settings_views.xml',
        'views/confirm_save_model_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'confirm_before_save/static/src/js/form_controller.js',
            'confirm_before_save/static/src/xml/confirm_dialog.xml',
            'confirm_before_save/static/src/css/confirm_save.css',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
