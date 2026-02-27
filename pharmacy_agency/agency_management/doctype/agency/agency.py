# Copyright (c) 2026, Abdul Hannan Shaikh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Agency(Document):

    def validate(self):
        if not self.is_active and self.agency_item:
            frappe.throw("Cannot deactivate Agency with linked items.")