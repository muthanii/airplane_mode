# Copyright (c) 2025, Muthana Alsaadi and contributors
# For license information, please see license.txt

import random

import frappe
from frappe.model.document import Document


class AirplaneTicket(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		from airplane_mode.airplane_mode.doctype.airplane_ticket_add_on_item.airplane_ticket_add_on_item import (
			AirplaneTicketAddonItem,
		)

		add_ons: DF.Table[AirplaneTicketAddonItem]
		amended_from: DF.Link | None
		departure_date: DF.Date
		departure_time: DF.Time
		destination_airport_code: DF.Data
		duration_of_flight: DF.Duration
		flight: DF.Link
		flight_price: DF.Currency
		gate_number: DF.Data | None
		passenger: DF.Link
		seat: DF.Data | None
		source_airport_code: DF.Data
		status: DF.Literal["Booked", "Checked-In", "Boarded", "Completed"]
		total_amount: DF.Currency
	# end: auto-generated types

	def before_save(self):
		self.total_amount = self.flight_price + sum(item.amount for item in self.add_ons or [])  # pyright: ignore[reportAttributeAccessIssue]

	def validate(self):
		# Prevent duplicate add-ons
		items = [d.item for d in self.add_ons]  # pyright: ignore[reportAttributeAccessIssue]
		if len(items) != len(set(items)):
			frappe.throw("Each add-on type must be unique.")

		# Prevent overboarding
		if self.flight:
			flight_doc = frappe.get_doc("Airplane Flight", self.flight)
			airplane_doc = frappe.get_doc("Airplane", flight_doc.airplane)  # pyright: ignore[reportAttributeAccessIssue]
			capacity = airplane_doc.capacity  # pyright: ignore[reportAttributeAccessIssue]

			# Count existing tickets (excluding this one if it's being updated)
			existing_tickets = frappe.db.count(
				"Airplane Ticket",
				{
					"flight": self.flight,
					"name": ["!=", self.name],  # Exclude current if updating
				},
			)

			if existing_tickets >= capacity:
				frappe.throw(
					f"Cannot create ticket: Flight has reached maximum capacity of {capacity} seats."
				)

	def before_submit(self):
		if self.status != "Boarded":
			frappe.throw("Cannot submit ticket unless status is 'Boarded'.")

	def before_insert(self):
		if not self.seat:
			number = random.randint(1, 99)
			letter = random.choice(["A", "B", "C", "D", "E"])
			self.seat = f"{number}{letter}"

	def on_submit(self):
		self.status = "Completed"
