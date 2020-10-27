# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version
from frappe import _

app_name = "land_planning_and_allocation"
app_title = "Land Planning And Allocation"
app_publisher = "Bantoo Accounting"
app_description = "Planning and allocation of land"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "duncan@thebantoo.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/land_planning_and_allocation/css/land_planning_and_allocation.css"
# app_include_js = "/assets/land_planning_and_allocation/js/land_planning_and_allocation.js"

# include js, css files in header of web template
# web_include_css = "/assets/land_planning_and_allocation/css/land_planning_and_allocation.css"
# web_include_js = "/assets/land_planning_and_allocation/js/land_planning_and_allocation.js"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "land_planning_and_allocation.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "land_planning_and_allocation.install.before_install"
# after_install = "land_planning_and_allocation.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "land_planning_and_allocation.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "Plot": {
        "after_insert": "land_planning_and_allocation.api.create_item",
        "validate": "land_planning_and_allocation.api.calculate_plot_details",
    },

    "Project":{
        "after_insert": "land_planning_and_allocation.api.create_warehouse",
        "after_insert": "land_planning_and_allocation.api.project_item"
    },
}

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"land_planning_and_allocation.tasks.all"
# 	],
# 	"daily": [
# 		"land_planning_and_allocation.tasks.daily"
# 	],
# 	"hourly": [
# 		"land_planning_and_allocation.tasks.hourly"
# 	],
# 	"weekly": [
# 		"land_planning_and_allocation.tasks.weekly"
# 	]
# 	"monthly": [
# 		"land_planning_and_allocation.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "land_planning_and_allocation.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "land_planning_and_allocation.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "land_planning_and_allocation.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]



fixtures = [
	{
		"dt": "Custom Script",
		"filters": [
			[
				"name", "in", [
					"Sales Invoice-Client"
				]
			]
		]

	},
	{
		"dt": "Warehouse",
        "filters": [
            [
                "warehouse_name", "in", [
                    "Bulk Land",
                    "Sales Land"
                ]
            ]
        ]
	},
	{
		"dt": "Project Type",
        "filters": [
            [
                "project_type", "in", [
                        "Land"
                    ]
            ]
        ]
	},
	{
		"dt": "Notification",
        "filters": [
            "is_standard != 1"
        ]
	},
	{
		"dt": "Custom Field",
		"filters": [
			[
				"name", "in", [
					"Sale Invoice Item-land_details",
					"Sale Invoice Item-plot_id",
					"Sale Invoice Item-column_break_7",
					"Sale Invoice Item-land_project",
					"Sale Invoice Item-subdivision",
					"Customer-nrc_number",
					"Project-map_section",
					"Project-map",
					"Project-coordinates_section",
					"Project-land_coordinates",
					"Project-project_land_details",
					"Project-area_sqm",
					"Project-ready_for_sale",
					"Project-project_subdivision",
					"Project-subdivision",
					"Item-land"

				]
			]
		]
	}
]