from django.test import Client
from django.test import TestCase
from django.urls import resolve

from lab_8.views import index

class Lab8UnitTest(TestCase):
    def test_lab_8_url_is_exist(self):
        response = Client().get('/lab-8/')
        self.assertEqual(response.status_code, 200)


    def test_lab8_using_index_func(self):
        found = resolve('/lab-8/')
        self.assertEqual(found.func, index)

    def test_lab8_using_right_template(self):
        response = self.client.get('/lab-8/')
        self.assertTemplateUsed(response, 'lab_9/session/login.html')

        session = self.client.session
        session['user_login'] = 'user'
        session['kode_identitas'] = 'npm'
        session.save()

        response = self.client.get('/lab-8/')
        self.assertTemplateUsed(response, 'lab_8/lab_8.html')