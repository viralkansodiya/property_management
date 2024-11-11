

import frappe
from frappe.model.mapper import get_mapped_doc
from frappe import _


@frappe.whitelist()
def create_task(source_name, target_doc = None):
    doclist = get_mapped_doc(
        "Asset",
        source_name,
        {
            "Asset": { "doctype": "Task" },
        },
        target_doc,
    )

    return doclist


from frappe import _


def get_dashboard_data(data):
	return {
		"non_standard_fieldnames": {"Asset Movement": "asset"},
		"transactions": [{"label": _("Movement"), "items": ["Asset Movement", "Task"]}],
	}
