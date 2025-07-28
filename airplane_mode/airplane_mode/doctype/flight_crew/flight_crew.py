# Copyright (c) 2025, Muthana Alsaadi and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FlightCrew(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from airplane_mode.airplane_mode.doctype.flight_crew_member.flight_crew_member import FlightCrewMember
		from frappe.types import DF

		airplane_ticket: DF.Link | None
		crew_members: DF.Table[FlightCrewMember]
		flight: DF.Link | None
		gate_number: DF.Data | None
	# end: auto-generated types

	pass
