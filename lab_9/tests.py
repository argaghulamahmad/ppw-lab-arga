import os

import requests
from django.test import Client
from django.test import TestCase
from django.urls import resolve

from lab_9.views import *
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
        response = Client().post('/lab-9/custom_auth/login/', {'username': os.environ.get("SSO_USERNAME"),
                                                               'password': os.environ.get("SSO_PASSWORD")})
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

    # # profile feature, if user logged in --- not solved yet
    # def test_profile_feature_case1(self):
    #     Client().post('/lab-9/custom_auth/login/',
    #                   {'username': os.environ.get("SSO_USERNAME"),
    #                    'password': os.environ.get("SSO_PASSWORD")})
    #     response = Client().get('/lab-9/profile/')
    #     self.assertEqual(response.status_code, 302)

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

    def test_add_session_drones(self):
        id = 1
        url_post = '/lab-9/add_session_drones/' + str(id) + '/'
        response = Client().post(url_post)
        self.assertRedirects(response, '/lab-9/profile/', status_code=302, target_status_code=302)

    def test_add_session_opticals(self):
        id = 1
        url_post = '/lab-9/add_session_opticals/' + str(id) + '/'
        response = Client().post(url_post)
        self.assertRedirects(response, '/lab-9/profile/', status_code=302, target_status_code=302)

    def test_add_session_soundcards(self):
        id = 1
        url_post = '/lab-9/add_session_soundcards/' + str(id) + '/'
        response = Client().post(url_post)
        self.assertRedirects(response, '/lab-9/profile/', status_code=302, target_status_code=302)

    # def test_del_session_drones(self):
    #     id = 1
    #     # url_post = '/lab-9/add_session_drones/' + str(id) + '/'
    #     # Client().post(url_post)
    #
    #     url_del = '/lab-9/del_session_drones/' + str(id) + '/'
    #     response = Client().post(url_del)
    #
    #     self.assertRedirects(response, '/lab-9/profile/', status_code=302, target_status_code=302)
    #
    #
    # def test_del_session_opticals(self):
    #     id = 1
    #     # url_post = '/lab-9/add_session_opticals/' + str(id) + '/'
    #     # Client().post(url_post)
    #
    #     url_del = '/lab-9/del_session_opticals/' + str(id) + '/'
    #     response = Client().post(url_del)
    #
    #     self.assertRedirects(response, '/lab-9/profile/', status_code=302, target_status_code=302)
    #
    #
    # def test_del_session_soundcards(self):
    #     id = 1
    #     # url_post = '/lab-9/add_session_soundcards/' + str(id) + '/'
    #     # Client().post(url_post)
    #
    #     url_del = '/lab-9/del_session_soundcards/' + str(id) + '/'
    #     response = Client().post(url_del)
    #
    #     self.assertRedirects(response, '/lab-9/profile/', status_code=302, target_status_code=302)
    #
    # def test_clear_session_drones(self):
    #     response = Client().post('/lab-9/clear_session_drones/')
    #     self.assertRedirects(response, '/lab-9/profile/', status_code=302, target_status_code=302)
    #
    # def test_clear_session_opticals(self):
    #     response = Client().post('/lab-9/clear_session_opticals/')
    #     self.assertRedirects(response, '/lab-9/profile/', status_code=302, target_status_code=302)
    #
    # def test_clear_session_soundcards(self):
    #     response = Client().post('/lab-9/clear_session_soundcards/')
    #     self.assertRedirects(response, '/lab-9/profile/', status_code=302, target_status_code=302)

    # def test_islogin_cookie(self):
    #     req = requests.post(reverse('lab-9:cookie/login/'), {'username': 'user', 'password': 'pass'})
    #     self.assertEqual(is_login(req), True)

    def test_clear_cookie(self):
        response = Client().post('/lab-9/cookie/clear/')
        self.assertRedirects(response, '/lab-9/cookie/login', target_status_code=301)

    def test_my_cookie_auth(self):
        self.assertEqual(my_cookie_auth('user', 'pass'), True)
