frappe.listview_settings['Agency'] = {
    get_indicator: function (doc) {
        if (!doc.is_active) {
            return ['Inactive', 'red'];
        } else {
            return ['Active', 'green'];
        }
    }
};