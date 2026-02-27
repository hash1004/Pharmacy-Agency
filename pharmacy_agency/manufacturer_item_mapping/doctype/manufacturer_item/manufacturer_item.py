# Copyright (c) 2026, Abdul Hannan Shaikh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ManufacturerItem(Document):
    def validate(self):
        manufacturer = frappe.get_doc("Agency Manufacturer", self.manufacturer)

        if manufacturer.is_blocked:
            frappe.throw("Item cannot be added since Manufacturer is blocked.")

        existing = frappe.db.exists(
            "Manufacturer Item",
            {
                "manufacturer": self.manufacturer,
                "item_code": self.item_code,
                "name": ["!=", self.name],
            },
        )

        if existing:
            frappe.throw(
                "Mapping already exists for this Item and Manufacturer."
            )  # noqa:E501

        if not self.part_no:
            self.part_no = self.item_code
