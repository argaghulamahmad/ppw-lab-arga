import os
import environ
import requests

from django.test import Client
from django.test import TestCase
from django.urls import resolve

from lab_9.csui_helper import get_access_token, get_client_id, verify_user, get_data_user, API_VERIFY_USER, \
    API_MAHASISWA
from lab_9.views import *

root = environ.Path(__file__) - 3 # three folder back (/a/b/c/ - 3 = /)
env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env('.env')

class Lab9UnitTest(TestCase):
    def test_lab_9_url_is_exist(self):
        response = Client().get('/lab-9/')
        self.assertEqual(response.status_code, 200)

    def test_lab9_using_index_func(self):
        found = resolve('/lab-9/')
        self.assertEqual(found.func, index)

    def test_lab9_using_right_template(self):
        response = self.client.get('/lab-9/')
        self.assertTemplateUsed(response, 'lab_9/session/login.html')

        session = self.client.session
        session['user_login'] = 'anotheruser'
        session['kode_identitas'] = 'npm'
        session.save()

        response = self.client.get('/lab-9/')
        self.assertEqual(response.status_code, 302)

    # test for enterkomputer api
    def test_get_enterkomputer_api1(self):
        response = requests.get('https://www.enterkomputer.com/api/product/drone.json')
        self.assertEqual(response.json(), get_drones().json())

    def test_get_enterkomputer_api2(self):
        response = requests.get('https://www.enterkomputer.com/api/product/soundcard.json')
        self.assertEqual(response.json(), get_soundcards().json())

    def test_get_enterkomputer_api3(self):
        response = requests.get('https://www.enterkomputer.com/api/product/optical.json')
        self.assertEqual(response.json(), get_opticals().json())

    # test csui_helper
    def test_verify_function(self):
        self.username = env("SSO_USERNAME")
        self.password = env("SSO_PASSWORD")
        access_token = get_access_token(self.username, self.password)
        parameters = {"access_token": access_token, "client_id": get_client_id()}
        response = requests.get(API_VERIFY_USER, params=parameters)
        result = verify_user(access_token)
        self.assertEqual(result, response.json())

    def test_get_data_user_function(self):
        self.username = env("SSO_USERNAME")
        self.password = env("SSO_PASSWORD")
        self.npm = env("NPM")
        access_token = get_access_token(self.username, self.password)
        parameters = {"access_token": access_token, "client_id": get_client_id()}
        response = requests.get(API_MAHASISWA + self.npm, params=parameters)
        result = get_data_user(access_token, self.npm)
        self.assertEqual(result, response.json())

    # test for custom_auth.py
    def test_auth_login_correct(self):
        response = Client().post('/lab-9/custom_auth/login/', {'username': os.environ.get("SSO_USERNAME"),
                                                               'password': os.environ.get("SSO_PASSWORD")})
        self.assertEqual(response.status_code, 302)

    def test_auth_login_wrong(self):
        response_post = self.client.post(reverse('lab-9:auth_login'), {'username': 'aku', 'password': 'ganteng'})
        response = self.client.get('/lab-9/')
        html_response = response.content.decode('utf8')
        self.assertIn('Username atau password salah', html_response)

    def test_auth_logout(self):
        self.username = env("SSO_USERNAME")
        self.password = env("SSO_PASSWORD")

        response_post = self.client.post(reverse('lab-9:auth_login'),
                                         {'username': self.username, 'password': self.password})
        response = self.client.post(reverse('lab-9:auth_logout'))
        response = self.client.get('/lab-9/')
        html_response = response.content.decode('utf8')
        self.assertIn('Anda berhasil logout. Semua session Anda sudah dihapus', html_response)

    # test for views.py
    def test_profile_feature(self):
        self.username = env("SSO_USERNAME")
        self.password = env("SSO_PASSWORD")

        response_post = self.client.post(reverse('lab-9:auth_login'),
                                         {'username': self.username, 'password': self.password})
        response = self.client.get('/lab-9/profile/')
        html_response = response.content.decode('utf8')
        self.assertIn('arga.ghulam', html_response)

    def test_profile_not_loggedin(self):
        response = self.client.get('/lab-9/profile/')
        self.assertEqual(response.status_code, 302)

    def test_cookie_login(self):
        self.username = env("SSO_USERNAME")
        self.password = env("SSO_PASSWORD")

        response_post = self.client.post(reverse('lab-9:auth_login'),
                                         {'username': self.username, 'password': self.password})

        response_post = self.client.get(reverse('lab-9:cookie_login'))
        self.assertTemplateUsed(response_post, 'lab_9/cookie/login.html')
        response_post = self.client.get(reverse('lab-9:cookie_auth_login'))
        self.assertEqual(response_post.status_code, 302)

        response_post = self.client.get(reverse('lab-9:cookie_profile'))
        self.assertEqual(response_post.status_code, 302)

        response_post = self.client.post(reverse('lab-9:cookie_auth_login'), {'username': '', 'password': ''})
        response_post = self.client.get(reverse('lab-9:cookie_login'))
        html_response = response_post.content.decode('utf8')
        self.assertIn('Username atau Password Salah', html_response)

        response_post = self.client.post(reverse('lab-9:cookie_auth_login'),
                                         {'username': 'user', 'password': 'pass'})
        response_post = self.client.get(reverse('lab-9:cookie_login'))
        response_post = self.client.get(reverse('lab-9:cookie_profile'))
        self.assertTemplateUsed(response_post, 'lab_9/cookie/profile.html')

        response = self.client.get(reverse('lab-9:cookie_profile'))
        response.client.cookies['user_login'] = 'wronguser'
        response_post = self.client.get(reverse('lab-9:cookie_profile'))
        self.assertTemplateUsed(response_post, 'lab_9/cookie/login.html')
        response_post = self.client.post(reverse('lab-9:cookie_auth_login'),
                                         {'username': 'user', 'password': 'pass'})
        response_post = self.client.get(reverse('lab-9:cookie_clear'))
        self.assertEqual(response_post.status_code, 302)

    def test_session_profile(self):
        response = Client().get('/lab-9/profile')
        self.assertEqual(response.status_code, 301)

    def test_add_delete_and_reset_favorite_drones(self):
        self.username = env("SSO_USERNAME")
        self.password = env("SSO_PASSWORD")

        response_post = self.client.post(reverse('lab-9:auth_login'),
                                         {'username': self.username, 'password': self.password})

        response_post = self.client.post(reverse('lab-9:add_session_drones', kwargs={'id': 107894}))
        response_post = self.client.post(reverse('lab-9:add_session_drones', kwargs={'id': 107893}))
        response_post = self.client.post(reverse('lab-9:profile'))
        response_post = self.client.post(reverse('lab-9:del_session_drones', kwargs={'id': 107894}))

        response = self.client.get('/lab-9/profile/')
        html_response = response.content.decode('utf8')
        self.assertIn('Berhasil hapus dari favorite', html_response)

        response_post = self.client.post(reverse('lab-9:clear_session_drones'))
        response = self.client.get('/lab-9/profile/')
        html_response = response.content.decode('utf8')
        self.assertIn('Berhasil reset favorite drones', html_response)

        response_post = self.client.post(reverse('lab-9:clear_session_drones'))
        response = self.client.get('/lab-9/profile/')
        html_response = response.content.decode('utf8')
        self.assertIn('Favorite drones kosong', html_response)

        response_post = self.client.post(reverse('lab-9:auth_logout'))

    def test_add_delete_add_reset_favourite_opticals(self):
        self.username = env("SSO_USERNAME")
        self.password = env("SSO_PASSWORD")

        response_post = self.client.post(reverse('lab-9:auth_login'),
                                         {'username': self.username, 'password': self.password})

        response_post = self.client.post(reverse('lab-9:add_session_opticals', kwargs={'id': 53496}))
        response_post = self.client.post(reverse('lab-9:add_session_opticals', kwargs={'id': 53495}))
        response_post = self.client.post(reverse('lab-9:profile'))
        response_post = self.client.post(reverse('lab-9:del_session_opticals', kwargs={'id': 53496}))

        response = self.client.get('/lab-9/profile/')
        html_response = response.content.decode('utf8')
        self.assertIn('Berhasil hapus dari favorite', html_response)

        response_post = self.client.post(reverse('lab-9:clear_session_opticals'))
        response = self.client.get('/lab-9/profile/')
        html_response = response.content.decode('utf8')
        self.assertIn('Berhasil reset favorite opticals', html_response)

        response_post = self.client.post(reverse('lab-9:clear_session_opticals'))
        response = self.client.get('/lab-9/profile/')
        html_response = response.content.decode('utf8')
        self.assertIn('Favorite opticals kosong', html_response)

        response_post = self.client.post(reverse('lab-9:auth_logout'))

    def test_add_delete_add_reset_favourite_soundcards(self):
        self.username = env("SSO_USERNAME")
        self.password = env("SSO_PASSWORD")

        response_post = self.client.post(reverse('lab-9:auth_login'),
                                         {'username': self.username, 'password': self.password})

        response_post = self.client.post(reverse('lab-9:add_session_soundcards', kwargs={'id': 4459}))
        response_post = self.client.post(reverse('lab-9:add_session_soundcards', kwargs={'id': 4458}))
        response_post = self.client.post(reverse('lab-9:profile'))
        response_post = self.client.post(reverse('lab-9:del_session_soundcards', kwargs={'id': 4459}))

        response = self.client.get('/lab-9/profile/')
        html_response = response.content.decode('utf8')
        self.assertIn('Berhasil hapus dari favorite', html_response)

        response_post = self.client.post(reverse('lab-9:clear_session_soundcards'))
        response = self.client.get('/lab-9/profile/')
        html_response = response.content.decode('utf8')
        self.assertIn('Berhasil reset favorite soundcards', html_response)

        response_post = self.client.post(reverse('lab-9:clear_session_soundcards'))
        response = self.client.get('/lab-9/profile/')
        html_response = response.content.decode('utf8')
        self.assertIn('Favorite soundcards kosong', html_response)

        response_post = self.client.post(reverse('lab-9:auth_logout'))
