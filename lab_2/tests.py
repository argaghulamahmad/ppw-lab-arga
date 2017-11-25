from django.test import Client
from django.test import TestCase
from django.urls import resolve

from .views import index, landing_page_content, mhs_name


class Lab2UnitTest(TestCase):
    def test_lab_2_url_is_exist(self):
        response = Client().get('/lab-2/')
        self.assertEqual(response.status_code, 200)

    def test_lab2_using_index_func(self):
        found = resolve('/lab-2/')
        self.assertEqual(found.func, index)

    def test_landing_page_content_is_written(self):
        # Content cannot be null
        self.assertIsNotNone(landing_page_content)

        # Content is filled with 30 characters at least
        self.assertTrue(len(landing_page_content) >= 30)

    def test_landing_page_is_completed(self):
        response = Client().get('/lab-2/')
        self.assertTemplateUsed(response, 'lab_9/session/login.html')

        session = self.client.session
        session['user_login'] = 'user'
        session['kode_identitas'] = 'npm'
        session.save()

        response = self.client.get('/lab-2/')
        html_response = response.content.decode('utf8')
        self.assertIn('Hello, this is ' + mhs_name + '.', html_response)
        self.assertIn(landing_page_content, html_response)
