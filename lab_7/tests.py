import datetime
import os
import environ

from django.test import Client
from django.test import TestCase
from django.urls import resolve, reverse

from lab_7.models import Friend
from lab_7.views import index
from lab_9.csui_helper import get_access_token

now = datetime.datetime.now()
root = environ.Path(__file__) - 3 # three folder back (/a/b/c/ - 3 = /)
env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env('.env')


class Lab7UnitTest(TestCase):
    def setUp(self):
        self.friend = Friend.objects.create(
            friend_name="ARGA GHULAM AHMAD", npm="1606821601"
        )

    def test_lab_7_using_index_func(self):
        found = resolve('/lab-7/')
        self.assertEqual(found.func, index)

    def test_lab7_using_right_template(self):
        response = Client().get('/lab-7/')
        self.assertTemplateUsed(response, 'lab_9/session/login.html')

        session = self.client.session
        session['user_login'] = 'user'
        session['kode_identitas'] = 'npm'

        self.username = env("SSO_USERNAME")
        self.password = env("SSO_PASSWORD")

        session['access_token'] = get_access_token(self.username, self.password)
        session.save()
        response = self.client.get('/lab-7/')
        self.assertTemplateUsed(response, 'lab_7/lab_7.html')

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
                'friends_json': '[{"model": "lab_7.friend", "pk": 1, "fields": {"friend_name": "ARGA GHULAM AHMAD", "npm": "1606821601", "added_at": "' + now.strftime("%Y-%m-%d") + '"}}]',
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

    def test_add_friend_case1(self):
        self.client.post('/lab-7/add-friend/', {
            'name': 'ARGA GHULAM AHMAD',
            'npm': '1606821601'
        })

    def test_add_friend_case2(self):
        response = self.client.post('/lab-7/add-friend/', {
            'name': 'arga ghulam ahmad',
            'npm': '09121998'
        })
        self.assertEqual(response.status_code, 200)

    def test_friend_description(self):
        session = self.client.session
        session['user_login'] = 'user'
        session['kode_identitas'] = 'npm'
        session.save()

        response = self.client.post('/lab-7/friend-description/0/')
        self.assertEqual(response.status_code, 200)
