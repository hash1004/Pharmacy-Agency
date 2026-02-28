import frappe


def create_items():
    items = [
        {"item_code": "Insulin", "item_group": "Products", "stock_uom": "Nos"},  # noqa
        {"item_code": "Crocin", "item_group": "Products", "stock_uom": "Nos"},
        {"item_code": "Aspirin", "item_group": "Products", "stock_uom": "Nos"},
    ]
    for i in items:
        if not frappe.db.exists("Item", i["item_code"]):
            frappe.get_doc({"doctype": "Item", **i}).insert(
                ignore_permissions=True
            )  # noqa
    frappe.db.commit()


def create_agencies():
    agencies = [
        {
            "agency_name": "HealthBridge Distributors",
            "territory": "All Territories",
            "primary_contact": "+91 8987654534",
            "is_active": 1,
            "agency_item": [
                {
                    "item_code": "Aspirin",
                    "min_order_qty": 10,
                    "lead_time_days": 10,
                },  # noqa
                {
                    "item_code": "Crocin",
                    "min_order_qty": 20,
                    "lead_time_days": 5,
                },  # noqa
            ],
        },
        {
            "agency_name": "PharmaLink Traders",
            "territory": "All Territories",
            "primary_contact": "+91 8987954534",
            "is_active": 1,
            "agency_item": [
                {
                    "item_code": "Insulin",
                    "min_order_qty": 20,
                    "lead_time_days": 40,
                },  # noqa
                {
                    "item_code": "Aspirin",
                    "min_order_qty": 10,
                    "lead_time_days": 25,
                },  # noqa
            ],
        },
        {
            "agency_name": "NovaHealth Supply",
            "territory": "All Territories",
            "primary_contact": "+91 8987954234",
            "is_active": 0,
        },
    ]
    for a in agencies:
        if not frappe.db.exists("Agency", a["agency_name"]):
            frappe.get_doc({"doctype": "Agency", **a}).insert(
                ignore_permissions=True
            )  # noqa
            frappe.db.commit()


def create_agency_manufacturers():
    agency_manufacturers = [
        {"manufacturer_name": "Cipla", "gln": "8901234500001", "is_blocked": 0},  # noqa
        {
            "manufacturer_name": "Pfizer",
            "gln": "8901234500002",
            "is_blocked": 0,
        },  # noqa
        {"manufacturer_name": "GMBH", "gln": "8901234500003", "is_blocked": 0},
    ]
    for a in agency_manufacturers:
        if not frappe.db.exists("Agency Manufacturer", a["manufacturer_name"]):
            frappe.get_doc({"doctype": "Agency Manufacturer", **a}).insert(
                ignore_permissions=True
            )  # noqa
    frappe.db.commit()


def create_manufacturer_items():
    manufacturer_items = [
        {
            "manufacturer": "Cipla",
            "item_code": "Insulin",
            "part_no": "CPL-INS-001",
            "gtin": "08901234500001",
        },
        {
            "manufacturer": "GMBH",
            "item_code": "Insulin",
            "gtin": "08901234500002",
        },
        {
            "manufacturer": "Pfizer",
            "item_code": "Crocin",
            "part_no": "PFR-CRN-001",
            "gtin": "08901234500003",
        },  # noqa
        {
            "manufacturer": "GMBH",
            "item_code": "Aspirin",
            "gtin": "08901234500004",
        },  # noqa
    ]
    for m in manufacturer_items:
        if not frappe.db.exists(
            "Manufacturer Item", m["manufacturer"], m["item_code"]
        ):  # noqa
            frappe.get_doc({"doctype": "Manufacturer Item", **m}).insert(
                ignore_permissions=True
            )  # noqa
    frappe.db.commit()
