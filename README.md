### Pharmacy Agency


### Setup Instructions:
1. I prefer Frappe installation with [Frappe Docker](https://github.com/frappe/frappe_docker/blob/main/docs/05-development/01-development.md)

2. Setup a site with the instrcutions provided in the Frappe Docker Docs.

3. Install ERPNext and then Pharmacy Agency App
```
bench get-app https://github.com/hash1004/Pharmacy-Agency
bench --site sitename install-app pharmacy_agency
```

### Note: 
- Manufacturer Doctype is already present in ERPNext so added the new doctype as Agency Manufacturer
- Tested with the following app versions:
```json
{
	"frappe": "15.100.0",
	"erpnext": "15.97.0"
}
```

### Testing Instructions:
1. Check the doctypes created.

2. Agency Doctype has 3 documents. "PharmaLink Traders" and "HealthBridge Distributors" have items in them if you uncheck "Is Active" you won't be able to save it.

3. "Create Supplier" button creates a Supplier into ERPNExt and redirects to that Supplier.

4. Inactive Agencies show in red.

5. Disable GMBH "Agency Manufacturer" and try creating "Manufacturer Item" with GMBH Agency Manufacturer it will throw an error.

6. Try creating "Manufacturer Item" with "Agency Manufacturer" GMBH and "Item Code" Aspirin it will throw an error.

7. Test api endpoint with this command ```bench --site sitename execute --args "{'Aspirin'}" pharmacy_agency.api.get_manufacturer_mappings```
