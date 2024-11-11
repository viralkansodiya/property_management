import frappe

field = [
    {
        "doctype" : "Custom Field",
        "dt" : "Task",
        "fieldname" : "assset",
        "label" : "Property",
        "fieldtype" : "Link",
        "options" : "Asset",
        "insert_after" : "Project",
        "is_system_generated" : 1
    }
]

def create_fields(field = None):
    for row in field:
        doc = frappe.get_doc(row)
        doc.insert()

# from property_management.api.Field.task import create_fields