import frappe

def rent_item(doc, event):
    rent_group = frappe.db.get_list('Item Group',filters={'name': "Rent"},fields=['name'],as_list=True)
    if not rent_group:
        new_rent_group = frappe.get_doc(dict(
            doctype = 'Item Group',
            item_group_name = "Rent"
        ))
        new_rent_group.save()

    rent = frappe.db.get_list('Item',filters={'asset': doc.name},fields=['asset'],as_list=True)
    
    if not rent:
        new_rent_item = frappe.get_doc(dict(
            doctype = 'Item',
            item_code = doc.name + ': ' + doc.asset_name + ' - ' + "Rent",
            item_name = doc.name + ': ' + doc.asset_name + ' - ' + "Rent",
            item_group = "Rent",
            stock_uom = "Nos",
            is_stock_item = 0,
            include_item_in_manufacturing = 0,
            is_fixed_asset = 0,
            is_rent_item = 1,
            asset = doc.name,
            gst_hsn_code = rent
        ))
        new_rent_item.save()

def validate(self, method):
    if not frappe.db.get_value("Item", self.item_code, "asset"):
        frappe.db.set_value("Item", self.item_code, "asset", self.name)
        frappe.db.set_value("Item", self.item_code, "asset_name", self.asset_name)

def on_trash(self, method):
    frappe.db.set_value("Item", self.item_code, "asset", "")
    frappe.db.set_value("Item", self.item_code, "asset_name", "")

