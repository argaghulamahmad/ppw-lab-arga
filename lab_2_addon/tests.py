from django.test import TestCase, Client
from django.urls import resolve

from lab_2_addon.views import bio_dict, index


class Lab2AddonUnitTest(TestCase):
    def test_lab_2_addon_url_is_exist(self):
        response = Client().get('/lab-2-addon/')
        self.assertEqual(response.status_code, 200)

    def test_lab2_addon_using_index_func(self):
        found = resolve('/lab-2-addon/')
        self.assertEqual(found.func, index)

    def test_lab2_addon_bio_dict(self):
        # Check whether bio_dict is not None Object
        self.assertIsNotNone(bio_dict)

        # Check whether bio_dict entry is less than 3 items
        self.assertTrue(len(bio_dict) >= 3)

        # Checking all element in family member
        for bio in bio_dict:
            # Name cannot be None
            self.assertIsNotNone(bio['subject'])
            self.assertIsNotNone(bio['value'])

            # Name cannot be integer
            self.assertIsNot(type(bio['value']), type(8))

    def test_lab2_addon_bio_shown_in_page(self):
        response = Client().get('/lab-2-addon/')
        self.assertTemplateUsed(response, 'lab_9/session/login.html')

        session = self.client.session
        session['user_login'] = 'test'
        session['kode_identitas'] = '123'
        session.save()
        response = self.client.get('/lab-2-addon/')
        html_response = response.content.decode('utf8')

        # Checking all family member is shown in page
        for bio in bio_dict:
            self.assertIn('<td class="subject">' + bio['subject'] + '</td>', html_response)
            self.assertIn('<td class="value">' + bio['value'] + '</td>', html_response)
