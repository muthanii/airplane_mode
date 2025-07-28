# Copyright (c) 2025, Muthana Alsaadi and contributors
# For license information, please see license.txt

# import frappe
from datetime import datetime

from frappe.model.document import Document


class RentPayment(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amount_paid: DF.Currency
		contract: DF.Link
		month_for: DF.Literal[
			"January",
			"February",
			"March",
			"April",
			"May",
			"June",
			"July",
			"August",
			"September",
			"October",
			"November",
			"December",
		]
		payment_date: DF.Date
		rent_amount: DF.Currency
	# end: auto-generated types

	pass

	def autoname(self):
		if self.payment_date:
			self.month_for = self.get_month_from_date(self.payment_date)  # pyright: ignore[reportAttributeAccessIssue]

		if self.contract and self.month_for:
			self.name = f"{self.contract}-{self.month_for}"

	def get_month_from_date(self, date_obj):
		if isinstance(date_obj, str):
			date_obj = datetime.strptime(date_obj, "%Y-%m-%d")
		return date_obj.strftime("%B")
