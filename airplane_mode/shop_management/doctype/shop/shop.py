# Copyright (c) 2025, Muthana Alsaadi and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator


class Shop(WebsiteGenerator):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		airport: DF.Link
		area_sqft: DF.Float
		is_published: DF.Check
		route: DF.Data | None
		shop_name: DF.Data
		shop_number: DF.Int
		shop_type: DF.Link
		status: DF.Literal["Available", "Occupied"]
		tenant: DF.Link
	# end: auto-generated types

	pass
