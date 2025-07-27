import random

import frappe


def execute():
	tickets = frappe.get_all("Airplane Ticket", filters={"seat": ["is", "set"]}, fields=["name"])
	print(f"Found {len(tickets)} tickets to update")

	for ticket in tickets:
		seat = f"{random.randint(1, 99)}{random.choice(['A', 'B', 'C', 'D', 'E'])}"
		frappe.db.set_value("Airplane Ticket", ticket.name, "seat", seat)

	print("Seats updated successfully.")
