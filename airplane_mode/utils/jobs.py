import frappe


def update_ticket_gates_in_background(flight_name, new_gate):
	tickets = frappe.get_all("Airplane Ticket", filters={"flight": flight_name}, fields=["name"])
	for ticket in tickets:
		frappe.db.set_value("Airplane Ticket", ticket.name, "gate_number", new_gate)
