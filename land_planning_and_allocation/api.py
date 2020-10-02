import frappe
from frappe import _   

def create_item(doc, method):

    doc = frappe.get_doc({
        "doctype": "Item",
        "item_group": doc.subdivision,
        "item_code": "Plot " + str(doc.plot_id),
        "land": 1,
        "is_stock_item": 1,
        "stock_uom": "Square Meter",
        "opening_stock": doc.area,
        "standard_rate": doc.plot_price,
        "is_purchase_item": 0,
        "is_sales_item": 1,
        "valuation_rate": doc.plot_price,
        "include_item_in_manufacturing": 0,
        "description": "Project: " + str(doc.project) + "<br \>" + "Subdivision: " + str(doc.subdivision) + "<br \>" + "Plot ID: " + str(doc.plot_id) + "<br \>" + "Dimensions: " + str(doc.dimensions) + "<br \>" + "Area: " + str(doc.area) + "sqm",
    })
    doc.flags.ignore_permission = True
    doc.insert()