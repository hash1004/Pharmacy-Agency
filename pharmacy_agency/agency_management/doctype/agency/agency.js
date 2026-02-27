// Copyright (c) 2026, Abdul Hannan Shaikh and contributors
// For license information, please see license.txt

frappe.ui.form.on("Agency", {
    refresh(frm) {
        frm.add_custom_button("Create Supplier", function () {
            frappe.call({
                method: "frappe.client.insert",
                args: {
                    doc: {
                        doctype: "Supplier",
                        supplier_name: frm.doc.agency_name,
                        supplier_type: "Company",
                    },
                },
            }).then((response) => {
                const supplier = response.message;
                frappe.set_route("Form", "Supplier", supplier.name);
            });
        });
    },
});
