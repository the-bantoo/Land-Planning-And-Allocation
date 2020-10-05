from __future__ import unicode_literals
from frappe import _

def get_data():

    config = [
        {
            "label": _("Sales"),
            "items": [
                {
                    "type": "doctype",
					"name": "Customer",
					"description": _("Customer Database."),
					"onboard": 1,
                },
                {
                    "type": "doctype",
                    "name": "Plot",
                    "label": _("Plot"),
                    "onboard": 1,
                }
            ]
        },
        {
            "label": _("Land Details"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Item",
                    "label": _("Plot Item"),
                },
                {
                    "type": "doctype",
                    "name": "Project",
                    "onboard": 1,
                },
                {
                    "type": "doctype",
                    "name": "Subdivision",
                    "label": _("Subdivision"),
                    "onboard": 1,
                }
            ]
        },
        {
            "label": _("Reports"),
            "items": [
                {
					"type": "report",
					"name": "Item-wise Sales Register",
					"is_query_report": True,
					"doctype": "Sales Invoice"
				},
                {
					"type": "report",
					"name": "Accounts Receivable",
					"doctype": "Sales Invoice",
					"is_query_report": True
				},
            ]
        },
        {
            "label": _("Setup"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Land Settings",
                    "label": _("Land Settings"),
                    "onboard": 1,
                },
            ]
        }
    ]
    return config