/*
frappe.listview_settings['Plot'] = {
	add_fields: ["status"],
	get_indicator: function(doc) {
		return [__(doc.status), {
			"Reserved": "orange",
			"Under Construction": "red",
			"Available": "green",
			"Completed": "darkgrey"
		}[doc.status], "status,=," + doc.status];
	}
};
/*
frappe.listview_settings['Plot'] = {
	add_fields: ["status", "value"],
	get_indicator: function(doc) {
		if (doc.status) {
			return [__("Status"), "grey", "value,>,0"];
		} else if (doc.end_of_life && doc.end_of_life < frappe.datetime.get_today()) {
			return [__("Expired"), "grey", "end_of_life,<,Today"];
		} else if (doc.has_variants) {
			return [__("Template"), "orange", "has_variants,=,Yes"];
		} else {
			return [__(doc.status),{"Available": "darkgrey"}];
		}
	},
};
*/

/*
  frappe.listview_settings['Sales Invoice'] = {
	add_fields: ["customer", "customer_name", "base_grand_total", "outstanding_amount", "due_date", "company",
		"currency", "is_return"],
	get_indicator: function(doc) {
		if(cint(doc.is_return)==1) {
			return [__("Return"), "darkgrey", "is_return,=,Yes"];
		} else if(flt(doc.outstanding_amount)==0) {
			return [__("Paid"), "green", "outstanding_amount,=,0"]
		} else if(flt(doc.outstanding_amount) < 0) {
			return [__("Credit Note Issued"), "darkgrey", "outstanding_amount,<,0"]
		}else if (flt(doc.outstanding_amount) > 0 && doc.due_date >= frappe.datetime.get_today()) {
			return [__("Unpaid"), "orange", "outstanding_amount,>,0|due_date,>,Today"]
		} else if (flt(doc.outstanding_amount) > 0 && doc.due_date < frappe.datetime.get_today()) {
			return [__("Overdue"), "red", "outstanding_amount,>,0|due_date,<=,Today"]
		}
	}
}

frappe.listview_settings['plot'] = {
	add_fields: ["status", "value", "subdivision", "project"],
		get_indicator: function(doc) {
			if(cint(doc.status)==1) {
				return [__("Under Construction"), "red", "is_return,=,Yes"];
			} else if(flt(doc.outstanding_amount)==0) {
				return [__("Reserved"), "orange", "outstanding_amount,=,0"]
			} else if(flt(doc.outstanding_amount) < 0) {
				return [__("Completed"), "darkgrey", "outstanding_amount,<,0"]
			}else if (flt(doc.outstanding_amount) > 0 && doc.due_date >= frappe.datetime.get_today()) {
				return [__("Available"), "green", "outstanding_amount,>,0|due_date,>,Today"]
			}
		}
}
*/


frappe.listview_settings['plot'] = {
	add_fields: ["status", "value", "subdivision", "project"],
		get_indicator: function(doc) {
			if(doc.status) {
				return [__("Available"), "red", "project,=,"];
			} /*else {
				return [__("Completed"), "darkgrey", "project,=,Roma Park"];
			}*/
		}
}