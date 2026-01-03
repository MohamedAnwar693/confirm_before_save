/** @odoo-module **/
import { FormController } from "@web/views/form/form_controller";
import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";
import { ConfirmationDialog } from "@web/core/confirmation_dialog/confirmation_dialog";

patch(FormController.prototype, {
    setup() {
        super.setup();
        this.dialog = useService("dialog");
        this.rpc = useService("rpc");
        this.notification = useService("notification");

        this.hasUnsavedChanges = false;
        this.isConfirmationEnabled = true;
        this.showIndicator = true;

        this.loadSettings();
    },

    async loadSettings() {
        try {
            const ICPSudo = await this.rpc("/web/dataset/call_kw", {
                model: "ir.config_parameter",
                method: "get_param",
                args: ["confirm_before_save.enable_save_confirmation", "True"],
                kwargs: {},
            });
            this.isConfirmationEnabled = ICPSudo === "True";

            const showIndicatorParam = await this.rpc("/web/dataset/call_kw", {
                model: "ir.config_parameter",
                method: "get_param",
                args: ["confirm_before_save.show_modified_indicator", "True"],
                kwargs: {},
            });
            this.showIndicator = showIndicatorParam === "True";
        } catch (error) {
            console.error("Error loading save confirmation settings:", error);
        }
    },

    onFieldChanged(field) {
        const result = super.onFieldChanged(...arguments);

        if (this.model.root.dirty) {
            this.hasUnsavedChanges = true;
            if (this.showIndicator) {
                this.updateModifiedIndicator(true);
            }
        }

        return result;
    },

    updateModifiedIndicator(show) {
        const formSheet = document.querySelector(".o_form_sheet");
        if (formSheet) {
            if (show) {
                formSheet.classList.add("o_form_modified");
            } else {
                formSheet.classList.remove("o_form_modified");
            }
        }
    },

    async beforeLeave() {
        if (!this.isConfirmationEnabled || !this.hasUnsavedChanges || !this.model.root.dirty) {
            return super.beforeLeave();
        }

        return new Promise((resolve) => {
            this.dialog.add(ConfirmationDialog, {
                title: "Unsaved Changes",
                body: "You have unsaved changes. What would you like to do?",
                confirm: async () => {
                    try {
                        await this.model.root.save();
                        this.hasUnsavedChanges = false;
                        this.updateModifiedIndicator(false);
                        this.notification.add("Changes saved successfully", {
                            type: "success",
                        });
                        resolve(true);
                    } catch (error) {
                        this.notification.add("Error saving changes", {
                            type: "danger",
                        });
                        resolve(false);
                    }
                },
                cancel: () => {
                    this.model.root.discard();
                    this.hasUnsavedChanges = false;
                    this.updateModifiedIndicator(false);
                    resolve(true);
                },
                close: () => {
                    resolve(false);
                },
                confirmLabel: "Save",
                cancelLabel: "Discard",
            });
        });
    },

    async saveButtonClicked(params = {}) {
        const result = await super.saveButtonClicked(params);
        if (result) {
            this.hasUnsavedChanges = false;
            this.updateModifiedIndicator(false);
        }
        return result;
    },

    async discard() {
        const result = await super.discard();
        this.hasUnsavedChanges = false;
        this.updateModifiedIndicator(false);
        return result;
    },
});