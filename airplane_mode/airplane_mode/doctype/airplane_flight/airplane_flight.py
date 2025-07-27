# Copyright (c) 2025, Muthana Alsaadi and contributors
# For license information, please see license.txt

import frappe
from frappe import enqueue
from frappe.website.website_generator import WebsiteGenerator

from airplane_mode.utils.jobs import update_ticket_gates_in_background


class AirplaneFlight(WebsiteGenerator):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from airplane_mode.airplane_mode.doctype.flight_crew_member.flight_crew_member import FlightCrewMember
		from frappe.types import DF

		airplane: DF.Link
		amended_from: DF.Link | None
		crew_members: DF.Table[FlightCrewMember]
		date_of_departure: DF.Date
		default_gate_number: DF.Data | None
		destination_airport: DF.Link
		destination_airport_code: DF.Data | None
		duration: DF.Duration
		is_published: DF.Check
		route: DF.Data | None
		source_airport: DF.Link
		source_airport_code: DF.Data | None
		status: DF.Literal["Scheduled", "Completed", "Cancelled"]
		time_of_departure: DF.Time
	# end: auto-generated types

	def on_submit(self):
		self.status = "Completed"

	def on_update(self):
		if self.has_value_changed("default_gate_number"):
			enqueue(
				update_ticket_gates_in_background,
				queue="default",
				flight_name=self.name,
				new_gate=self.default_gate_number,
				timeout=300,
			)
			frappe.msgprint("Ticket update job has been queued.")
