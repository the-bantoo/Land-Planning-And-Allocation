<<<<<<< HEAD

frappe.listview_settings['Plot'] = {
	add_fields: ["status"],
	get_indicator: function(doc) {
		return [__(doc.status), {
=======
/*frappe.listview_settings['Plot'] = {
	add_fields: ["status"],
	get_indicator: function(plot) {
		return [__(plot.status), {
>>>>>>> Doctype Modification
			"Reserved": "orange",
			"Under Construction": "red",
			"Available": "green",
			"Completed": "darkgrey"
<<<<<<< HEAD
		}[doc.status], "status,=," + doc.status];
	}
};
=======
		}[plot.status], "status,=," + plot.status];
	}
};


frappe.listview_settings['Item'] = {
	add_fields: ["item_name", "stock_uom", "item_group", "image", "variant_of",
		"has_variants", "end_of_life", "disabled"],
	filters: [["disabled", "=", "0"]],

	get_indicator: function(doc) {
		if (doc.disabled) {
			return [__("Disabled"), "grey", "disabled,=,Yes"];
		} else if (doc.end_of_life && doc.end_of_life < frappe.datetime.get_today()) {
			return [__("Expired"), "grey", "end_of_life,<,Today"];
		} else if (doc.has_variants) {
			return [__("Template"), "orange", "has_variants,=,Yes"];
		} else if (doc.variant_of) {
			return [__("Variant"), "green", "variant_of,=," + doc.variant_of];
		}
	}
};
*/

frappe.listview_settings['Plot'] = {
	add_fields: ["status", "plot_id", "plot_type", "plot_no", "area", "project", "subdivision"],

	get_indicator: function(doc) {
		if (doc.area == 25000) {
			return [__("Under Construction"), "red"];
		} else if (doc.area == 120) {
			return [__("Completed"), "orange"];
		} else if(doc.area == 180){
			return [__("Completed"), "darkgrey"]
		} else{
			return [__("Available"), "green"]
		}
}
};

//Green For Available
//Orange For Reserved: Paid Amount > 0
//Red For Under Construction: Project Status > 5%
//Gray for Construction Completed: Project Status > 95%


/*
frappe.listview_settings['Plot'] = {
	add_fields: ["status", "plot_id", "plot_type", "plot_no", "area", "project", "subdivision"],
	//filters: [["disabled", "=", "0"]],

	get_indicator: function(doc) {
		if (doc.area) {
			return [__("Under Construction"), "red", "area,>=,1000"];
		} else if (doc.end_of_life && doc.end_of_life < frappe.datetime.get_today()) {
			return [__("Completed"), "grey", "end_of_life,<,Today"];
		} else if (doc.has_variants) {
			return [__("Reserved"), "orange", "has_variants,=,Yes"];
		} else if (doc.variant_of) {
			return [__("Available"), "green", "variant_of,=," + doc.variant_of];
		}
	}
};
*/
>>>>>>> Doctype Modification
