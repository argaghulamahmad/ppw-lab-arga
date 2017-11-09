from django.test import Client
from django.test import TestCase
from django.urls import resolve

from lab_7.views import index


class Lab7UnitTest(TestCase):
    def test_lab_7_url_is_exist(self):
        response = Client().get('/lab-7/')
        self.assertEqual(response.status_code, 200)

    def test_lab_7_using_index_func(self):
        found = resolve('/lab-7/')
        self.assertEqual(found.func, index)