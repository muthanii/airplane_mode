// Copyright (c) 2025, Muthana Alsaadi and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
	refresh(frm) {
		frm.add_custom_button("Assign Seat", () => {
			frappe.prompt(
				[
					{
						fieldname: "seat_number",
						label: "Seat Number",
						fieldtype: "Data",
						reqd: true,
					},
				],
				(values) => {
					frm.set_value("seat", values.seat_number);
					frm.save();
				},
				"Assign Seat"
			);
		});
	},
});
