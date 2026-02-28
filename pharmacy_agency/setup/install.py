from pharmacy_agency.setup.setup import (
    create_items,
    create_agencies,
    create_agency_manufacturers,
    create_manufacturer_items,
)  # noqa

def install_demo_data(*args):
    create_items()
    create_agencies()
    create_agency_manufacturers()
    create_manufacturer_items()
    