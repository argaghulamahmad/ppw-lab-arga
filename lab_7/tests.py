import os
from django.test import Client
from django.test import TestCase
from django.urls import resolve

from lab_7.api_csui_helper.csui_helper import CSUIhelper
from lab_7.views import index


class Lab7UnitTest(TestCase):
    def test_lab_7_url_is_exist(self):
        response = Client().get('/lab-7/')
        self.assertEqual(response.status_code, 200)

    def test_lab_7_using_index_func(self):
        found = resolve('/lab-7/')
        self.assertEqual(found.func, index)

    def test_wrong_username_password(self):
        csui_helper = CSUIhelper("wrongusername",
                                 "wrongpassword")
        csui_helper.instance.username = "wrongusername"
        csui_helper.instance.password = "wrongpassword"
        csui_helper.instance.get_access_token()

    def test_get_client_id(self):
        csui_helper = CSUIhelper(os.environ.get("SSO_USERNAME"),
                                 os.environ.get("SSO_PASSWORD"))
        self.assertEqual(csui_helper.instance.get_client_id, csui_helper.instance.client_id)

    def test_set_current_page(self):
        csui_helper = CSUIhelper(os.environ.get("SSO_USERNAME"),
                                 os.environ.get("SSO_PASSWORD"))
        page_number = 3
        csui_helper.instance.set_current_page(page_number)
        self.assertEqual(csui_helper.instance.current_page_number, page_number)

    def test_get_auth_param_dict(self):
        csui_helper = CSUIhelper(os.environ.get("SSO_USERNAME"),
                                 os.environ.get("SSO_PASSWORD"))
        dict = csui_helper.instance.get_auth_param_dict()
        # self.assertEqual(dict['access_token'], csui_helper.instance.access_token)
        # self.assertEqual(dict['client_id'], csui_helper.instance.client_id)

