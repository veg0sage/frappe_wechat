# -*- coding: utf-8 -*-
# Copyright (c) 2017, Dirk Chang and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from wechatpy.oauth import WeChatOAuth
from wechat.api import check_wechat_binding


def get_context(context):
	context.no_cache = 1

	url = "/desk#List/Tickets Ticket"
	if frappe.form_dict.name:
		url = url + "/" + frappe.form_dict.name
	check_wechat_binding(redirect_url=url)

