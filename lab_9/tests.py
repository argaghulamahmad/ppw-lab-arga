import os
from django.test import Client
from django.test import TestCase
from django.urls import resolve

from lab_9.views import index
from lab_9.api_enterkomputer import get_soundcards, get_opticals, get_drones
from lab_9.csui_helper import get_access_token, get_client_id, verify_user, get_data_user

class Lab9UnitTest(TestCase):
    def test_lab_9_url_is_exist(self):
        response = Client().get('/lab-9/')
        self.assertEqual(response.status_code, 200)


    def test_lab9_using_index_func(self):
        found = resolve('/lab-9/')
        self.assertEqual(found.func, index)

    # test for enterkomputer api

    def test_get_enterkomputer_api(self):
        self.assertJSONNotEqual(str(get_drones().content, encoding='utf8'), {})
        self.assertJSONNotEqual(str(get_opticals().content, encoding='utf8'), {})
        self.assertJSONNotEqual(str(get_soundcards().content, encoding='utf8'), {})

    # test for csui_helper.py

    def test_get_client_id(self):
        self.assertEqual(get_client_id(), 'X3zNkFmepkdA47ASNMDZRX3Z9gqSU1Lwywu5WepG')

    def test_verify_user(self):
        access_token = get_access_token(os.environ.get("SSO_USERNAME"),
                                 os.environ.get("SSO_PASSWORD"))

        self.assertNotEqual((verify_user(access_token)), {})

    def test_get_data_user(self):
        access_token = get_access_token(os.environ.get("SSO_USERNAME"),
                                        os.environ.get("SSO_PASSWORD"))

        self.assertNotEqual((get_data_user(access_token, get_client_id())), {})

    # test for custom_auth.py
    def test_auth_login_correct(self):
        response = Client().post('/lab-9/custom_auth/login/', {'username': os.environ.get("SSO_USERNAME"), 'password': os.environ.get("SSO_PASSWORD")})
        self.assertEqual(response.status_code, 302)

    def test_auth_login_wrong(self):
        response = Client().post('/lab-9/custom_auth/login/', {'username': 'user', 'password': 'pass'})
        self.assertEqual(response.status_code, 302)

    def test_auth_logout(self):
        response = Client().get('/lab-9/custom_auth/logout/')
        self.assertEqual(response.status_code, 302)


    # test for views.py
    def test_profile_feature(self):
        response = Client().get('/lab-9/profile/')
        self.assertEqual(response.status_code, 302)

    def test_cookie_login(self):
        response = Client().get('/lab-9/cookie/login/')
        self.assertEqual(response.status_code, 200)

    def test_session_login(self):
        response = Client().get('/lab-9/cookie/auth_login/')
        self.assertEqual(response.status_code, 302)

    def test_cookie_profile(self):
        response = Client().get('/lab-9/cookie/profile')
        self.assertEqual(response.status_code, 301)

    def test_session_profile(self):
        response = Client().get('/lab-9/profile')
        self.assertEqual(response.status_code, 301)
