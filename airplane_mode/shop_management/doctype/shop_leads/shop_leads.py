# Copyright (c) 2025, Muthana Alsaadi and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ShopLeads(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		email: DF.Data | None
		full_name: DF.Data
		message: DF.SmallText | None
		phone: DF.Data | None
		shop: DF.Link
	# end: auto-generated types

	pass
