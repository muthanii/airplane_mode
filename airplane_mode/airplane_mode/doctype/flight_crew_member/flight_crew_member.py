# Copyright (c) 2025, Muthana Alsaadi and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FlightCrewMember(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		crew_member: DF.Data | None
		designation: DF.Data | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
	# end: auto-generated types

	pass
