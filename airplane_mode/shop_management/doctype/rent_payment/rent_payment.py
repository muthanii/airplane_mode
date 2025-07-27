# Copyright (c) 2025, Muthana Alsaadi and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class RentPayment(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amount_paid: DF.Currency
		contract: DF.Link | None
		month_for: DF.Data | None
		payment_date: DF.Date | None
	# end: auto-generated types

	pass
