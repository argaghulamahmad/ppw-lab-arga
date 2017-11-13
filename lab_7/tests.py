import os
from django.test import Client
from django.test import TestCase
from django.urls import resolve, reverse

from lab_7.api_csui_helper.csui_helper import CSUIhelper
from lab_7.models import Friend
from lab_7.views import index, model_to_dict


class Lab7UnitTest(TestCase):
    def setUp(self):
        self.friend = Friend.objects.create(
            friend_name="ARGA GHULAM AHMAD", npm="1606821601"
        )

    def test_lab_7_url_is_exist(self):
        response = Client().get('/lab-7/')
        self.assertEqual(response.status_code, 200)

    def test_lab_7_using_index_func(self):
        found = resolve('/lab-7/')
        self.assertEqual(found.func, index)

    def test_index_func(self):
        response = self.client.post('/lab-7/index', {
                    'buttonUrl': 2
                })

    def test_wrong_username_password(self):
        csui_helper = CSUIhelper("wrongusername",
                                 "wrongpassword")
        csui_helper.instance.username = "wrongusername"
        csui_helper.instance.password = "wrongpassword"
        csui_helper.instance.get_access_token()

    def test_get_client_id(self):
        csui_helper = CSUIhelper(os.environ.get("SSO_USERNAME"),
                                 os.environ.get("SSO_PASSWORD"))
        # self.assertEqual(csui_helper.instance.get_client_id, csui_helper.instance.client_id)

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

    def test_friend_list(self):
        response = Client().get('/lab-7/get-friend-list/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lab_7/daftar_teman.html')

    def test_get_friend_list_objects_json(self):
        response = self.client.get('/lab-7/get-friend-list-json/')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {
                'friends_json': '[{"model": "lab_7.friend", "pk": 1, "fields": {"friend_name": "ARGA GHULAM AHMAD", "npm": "1606821601", "added_at": "2017-11-13"}}]',
                'status': 'success'}
        )

    def test_delete_friend(self):
        response = self.client.post('/lab-7/delete-friend/')
        self.assertEqual(response.status_code, 200)

    def test_validate_npm(self):
        response = self.client.post('/lab-7/validate-npm/', {
                    'npm': 1606821601
                })
        self.assertEqual(response.status_code, 200)
