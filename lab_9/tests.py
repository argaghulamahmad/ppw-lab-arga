from django.test import Client
from django.test import TestCase
from django.urls import resolve

from lab_9.views import index

class Lab9UnitTest(TestCase):
    def test_lab_9_url_is_exist(self):
        response = Client().get('/lab-9/')
        self.assertEqual(response.status_code, 200)


    def test_lab9_using_index_func(self):
        found = resolve('/lab-9/')
        self.assertEqual(found.func, index)