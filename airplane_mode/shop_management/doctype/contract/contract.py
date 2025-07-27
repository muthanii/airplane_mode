# Copyright (c) 2025, Muthana Alsaadi and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Contract(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		end_date: DF.Date | None
		is_active: DF.Check
		rent_amount: DF.Currency
		shop: DF.Link | None
		start_date: DF.Date | None
		tenant: DF.Link | None
	# end: auto-generated types

	pass
