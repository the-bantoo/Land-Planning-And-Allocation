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
*/



frappe.listview_settings['plot'] = {
	add_fields: ["status", "project", "plot_type", "subdivision"],
	get_indicator: function(doc) {
		if(doc.status) {
			return [__("Reserved"), "green", "status,=,Reserved"];
		} /*else if(flt(doc.outstanding_amount)==0) {
			return [__("Paid"), "green", "outstanding_amount,=,0"]
		} else if(flt(doc.outstanding_amount) < 0) {
			return [__("Credit Note Issued"), "darkgrey", "outstanding_amount,<,0"]
		}else if (flt(doc.outstanding_amount) > 0 && doc.due_date >= frappe.datetime.get_today()) {
			return [__("Unpaid"), "orange", "outstanding_amount,>,0|due_date,>,Today"]
		} else if (flt(doc.outstanding_amount) > 0 && doc.due_date < frappe.datetime.get_today()) {
			return [__("Overdue"), "red", "outstanding_amount,>,0|due_date,<=,Today"]
		}*/
	}
}