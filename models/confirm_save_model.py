from odoo import models, fields, api


class ConfirmSaveModel(models.Model):
    _name = 'confirm.save.model'
    _description = 'Model Configuration for Save Confirmation'
    _rec_name = 'model_id'

    model_id = fields.Many2one(
        'ir.model',
        string='Model',
        required=True,
        ondelete='cascade',
        help='Select the model for which save confirmation should be enabled'
    )

    model_name = fields.Char(
        related='model_id.model',
        string='Model Name',
        store=True,
        readonly=True
    )

    require_confirmation = fields.Boolean(
        string='Require Confirmation',
        default=True,
        help='If enabled, users will be prompted before auto-save on this model'
    )

    active = fields.Boolean(
        string='Active',
        default=True,
        help='Uncheck to disable save confirmation for this model'
    )

    _sql_constraints = [
        ('model_unique', 'unique(model_id)', 'This model is already configured!')
    ]

    @api.model
    def get_enabled_models(self):
        records = self.search([('require_confirmation', '=', True), ('active', '=', True)])
        return records.mapped('model_name')

    @api.model
    def is_model_enabled(self, model_name):
        return self.search_count([
            ('model_name', '=', model_name),
            ('require_confirmation', '=', True),
            ('active', '=', True)
        ]) > 0