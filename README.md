# Confirm Before Save - Odoo 19 Module

## Problem Statement

Odoo's default auto-save functionality causes a common and frustrating problem for users:

- **Accidental changes are saved automatically** when navigating away from forms
- **No confirmation dialog** warns users about unsaved changes
- **Data integrity issues** arise from unintended edits
- **Training difficulties** for new users who expect explicit save actions

This module solves these issues by adding a confirmation system before auto-save occurs.

## Features

✅ **Confirmation Dialog** - Shows a clear dialog when navigating away with unsaved changes  
✅ **Visual Indicators** - Displays "Unsaved Changes" indicator when form is modified  
✅ **Three-Option Dialog** - Save, Discard, or Cancel navigation  
✅ **Global Settings** - Enable/disable features company-wide  
✅ **Per-Model Configuration** - Control which models require confirmation  
✅ **Easy to Use** - Works automatically with all standard Odoo forms  
✅ **Non-Intrusive** - Only activates when there are actual unsaved changes

## Installation

1. Copy the `confirm_before_save` folder to your Odoo addons directory
2. Update the apps list: Go to Apps → Update Apps List
3. Search for "Confirm Before Save"
4. Click Install

## Configuration

### Global Settings

Navigate to: **Settings → General Settings → Confirm Before Save**

- **Enable Save Confirmation**: Show confirmation dialog when navigating away (Default: ON)
- **Show Modified Indicator**: Display visual indicator for unsaved changes (Default: ON)

### Per-Model Configuration

Navigate to: **Settings → Technical → Model Save Confirmation**

Add models that should require save confirmation:
1. Click "Create"
2. Select the model (e.g., Sales Order, Contact, Product)
3. Enable "Require Confirmation"
4. Save

## Usage

Once installed and configured:

1. **Editing a Form**: When you edit any field, you'll see an "Unsaved Changes" indicator
2. **Navigating Away**: If you try to navigate (click menu, switch records, etc.), a dialog appears
3. **Choose Action**:
   - **Save**: Saves your changes and continues navigation
   - **Discard**: Discards changes and continues navigation
   - **Cancel**: Stays on the current page

## Technical Details

### Module Structure

```
confirm_before_save/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── res_config_settings.py
│   └── confirm_save_model.py
├── views/
│   ├── res_config_settings_views.xml
│   └── confirm_save_model_views.xml
├── security/
│   └── ir.model.access.csv
├── static/
│   └── src/
│       ├── js/
│       │   └── form_controller.js
│       ├── css/
│       │   └── confirm_save.css
│       └── xml/
│           └── confirm_dialog.xml
└── README.md
```

### Key Components

- **FormController Patch**: Intercepts navigation events in form views
- **Config Parameters**: Store global settings
- **Model Configuration**: Database model for per-model settings
- **Visual CSS**: Provides clear indicators for modified forms

## Compatibility

- **Odoo Version**: 19.0
- **Dependencies**: base, web
- **License**: LGPL-3

## Benefits

- ✅ Prevents accidental data loss
- ✅ Improves data integrity
- ✅ Reduces user frustration
- ✅ Makes Odoo behavior more predictable
- ✅ Easier onboarding for new users
- ✅ Aligns with user expectations from other software

## Support

For issues, questions, or feature requests:
- Check the Odoo documentation
- Review the code comments
- Contact your Odoo administrator

## Credits

**Author**: Mohamed Anwar  
**Version**: 19.0.1.0.0  
**License**: LGPL-3

---

**Note**: This module addresses a widely reported usability issue in Odoo. It provides a safety net without breaking Odoo's workflow, giving users control over when their data is saved.