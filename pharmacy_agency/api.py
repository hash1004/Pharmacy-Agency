import frappe


@frappe.whitelist()
def get_manufacturer_mappings(item_code):
    return frappe.db.get_list(
        "Manufacturer Item",
        filters={"item_code": item_code},
        fields=["name", "manufacturer", "part_no", "gtin"],
    )
