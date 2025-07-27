# Copyright (c) 2025, Muthana Alsaadi and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Shop(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		airport: DF.Link | None
		area_sqft: DF.Float
		shop_name: DF.Data | None
		shop_number: DF.Data | None
		shop_type: DF.Link | None
		status: DF.Literal["Available", "Occupied"]
		tenant: DF.Link | None
	# end: auto-generated types

	pass
