# Copyright (c) 2025, Muthana Alsaadi and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
	columns = [
		{
			"label": _("Airline"),
			"fieldname": "airline",
			"fieldtype": "Link",
			"options": "Airline",
			"width": 200,
		},
		{"label": _("Revenue"), "fieldname": "revenue", "fieldtype": "Currency", "width": 150},
	]

	# Step 1: Get all Airlines
	airlines = frappe.get_all("Airline", fields=["name"])

	data = []

	# Step 2: Loop and calculate revenue for each airline
	for airline in airlines:
		revenue = (
			frappe.db.get_value(
				"Airplane Ticket", filters={"airline": airline.name}, fieldname="sum(total_amount)"
			)
			or 0
		)

		data.append({"airline": airline.name, "revenue": revenue})

	# Step 3: Total revenue
	total_revenue = sum(d["revenue"] for d in data)

	# Step 4: Donut chart
	chart = {
		"data": {
			"labels": [d["airline"] for d in data],
			"datasets": [{"values": [d["revenue"] for d in data]}],
		},
		"type": "donut",
	}

	# Step 5: Report summary
	report_summary = [{"label": "Total Revenue", "value": total_revenue, "indicator": "green"}]

	return columns, data, None, chart, report_summary
