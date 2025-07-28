# Copyright (c) 2025, Muthana Alsaadi and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Contract(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		end_date: DF.Date
		is_active: DF.Check
		rent_amount: DF.Currency
		shop: DF.Link
		start_date: DF.Date
		tenant: DF.Link
	# end: auto-generated types

	pass

	def validate(self):
		self.rent_amount = frappe.get_doc("Shop Settings").default_rent_amount  # type: ignore
