from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    enable_save_confirmation = fields.Boolean(
        string='Enable Save Confirmation',
        config_parameter='confirm_before_save.enable_save_confirmation',
        default=True,
        help='Show confirmation dialog when navigating away with unsaved changes'
    )

    show_modified_indicator = fields.Boolean(
        string='Show Modified Indicator',
        config_parameter='confirm_before_save.show_modified_indicator',
        default=True,
        help='Display visual indicator when form has unsaved changes'
    )

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        res.update(
            enable_save_confirmation=ICPSudo.get_param(
                'confirm_before_save.enable_save_confirmation', 'True'
            ) == 'True',
            show_modified_indicator=ICPSudo.get_param(
                'confirm_before_save.show_modified_indicator', 'True'
            ) == 'True',
        )
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        ICPSudo.set_param(
            'confirm_before_save.enable_save_confirmation',
            self.enable_save_confirmation
        )
        ICPSudo.set_param(
            'confirm_before_save.show_modified_indicator',
            self.show_modified_indicator
        )