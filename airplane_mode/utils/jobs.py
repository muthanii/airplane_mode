from datetime import datetime

import frappe


def update_ticket_gates_in_background(flight_name, new_gate):
	tickets = frappe.get_all("Airplane Ticket", filters={"flight": flight_name}, fields=["name"])
	for ticket in tickets:
		frappe.db.set_value("Airplane Ticket", ticket.name, "gate_number", new_gate)


def send_rent_reminders():
	settings = frappe.get_single("Shop Settings")
	if not settings.enable_rent_reminders:  # type: ignore[attr-defined]
		frappe.logger().info("Rent reminders disabled in settings.")
		return

	month_str = datetime.today().strftime("%B %Y")  # e.g., July 2025
	active_contracts = frappe.get_all(
		"Contract", filters={"is_active": 1}, fields=["name", "tenant", "shop", "rent_amount"]
	)

	for contract in active_contracts:
		# Skip if already paid this month
		rent_exists = frappe.db.exists("Rent Payment", {"contract": contract.name, "month_for": month_str})

		if rent_exists:
			frappe.logger().info(f"Rent already paid for {contract.name} in {month_str}")
			continue

		tenant = frappe.get_doc("Tenant", contract.tenant)
		if not tenant.email:  # pyright: ignore[reportAttributeAccessIssue]
			frappe.logger().warning(f"Tenant {tenant.name} has no email. Skipping.")
			continue

		tenant_name = tenant.tenant_name  # pyright: ignore[reportAttributeAccessIssue]
		# Send email
		try:
			frappe.sendmail(
				recipients=[tenant.email],  # pyright: ignore[reportAttributeAccessIssue]
				subject=f"Rent Reminder for Shop: {contract.shop}",
				message=f"""
Dear {tenant_name},<br><br>
This is a reminder that your rent of <b>{contract.rent_amount}</b> for the month of <b>{month_str}</b> is due.<br>
Please ensure timely payment.<br><br>
Regards,<br>Airport Admin
                """,
			)
			frappe.logger().info(f"Rent reminder sent to {tenant.email} for contract {contract.name}")  # pyright: ignore[reportAttributeAccessIssue]

		except Exception as e:
			frappe.logger().error(f"Failed to send reminder to {tenant.email}: {e!s}")  # pyright: ignore[reportAttributeAccessIssue]
