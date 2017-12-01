from django.test import TestCase, Client
from django.urls import resolve, reverse

from lab_10.models import Pengguna
from lab_10.omdb_api import search_movie, get_detail_movie
from lab_10.utils import get_list_movie_from_api
from lab_10.views import index


class Lab10UnitTest(TestCase):
    def test_lab_10_url_is_exist(self):
        response = Client().get('/lab-10/')
        self.assertEqual(response.status_code, 200)

    def test_lab10_using_index_func(self):
        found = resolve('/lab-10/')
        self.assertEqual(found.func, index)

    # OMDB API TEST
    def test_search_movie_case1(self):
        data_search_movie = search_movie('Cars 3', '2017')
        self.assertNotEqual(data_search_movie, [])

    def test_search_movie_case2(self):
        data_search_movie = search_movie('Taken', '-')
        self.assertNotEqual(data_search_movie, [])

    def test_get_detail_movie(self):
        movie_detail = get_detail_movie('tt1985966')
        self.assertEqual(movie_detail['title'], b'Cloudy with a Chance of Meatballs 2')

    # utils.py test
    def test_get_list_movie_from_api(self):
        my_list = ['tt1985966']
        list_movies = get_list_movie_from_api(my_list)
        self.assertEqual(list_movies[0]['title'], b'Cloudy with a Chance of Meatballs 2')

    # views.py test
    def setUp(self):
        self.user = Pengguna.objects.create(
            kode_identitas='1606821601',
            nama="arga.ghulam",
        )

    def test_lab_10_using_right_template(self):
        response = self.client.get('/lab-10/')
        self.assertTemplateUsed(response, 'lab_10/session/login.html')

        session = self.client.session
        session['user_login'] = 'arga.ghulam'
        session['kode_identitas'] = '1606821601'
        session['role'] = 'mahasiswa'
        session.save()

        response = self.client.get('/lab-10/')
        self.assertEqual(response.status_code, 302)

    def test_dashboard_case1(self):
        response = self.client.get(reverse('lab-10:dashboard'))
        self.assertEqual(response.status_code, 302)

    def test_dashboard_case2(self):
        session = self.client.session
        session['user_login'] = 'arga.ghulam'
        session['kode_identitas'] = '1606821601'
        session['role'] = 'mahasiswa'
        session['movies'] = ['tt1985966', 'tt1981128']
        session.save()

        response = self.client.get(reverse('lab-10:dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_case3(self):
        session = self.client.session
        session['user_login'] = 'arga.cerdas'
        session['kode_identitas'] = '1606821998'
        session['role'] = 'mahasiswa'
        session.save()

        response = self.client.get(reverse('lab-10:dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_add_watch_later_case1(self):
        session = self.client.session
        session['user_login'] = 'arga.ghulam'
        session['kode_identitas'] = '1606821601'
        session['role'] = 'mahasiswa'
        session.save()

        response = self.client.post(reverse('lab-10:add_watch_later', kwargs={'id': 'tt1981128'}))
        self.assertEqual(response.status_code, 302)

    def test_add_watch_later_case2(self):
        session = self.client.session
        session['user_login'] = 'arga.ghulam'
        session['kode_identitas'] = '1606821601'
        session['role'] = 'mahasiswa'
        session.save()

        response = self.client.post(reverse('lab-10:add_watch_later', kwargs={'id': 'tt1981128'}))
        response = self.client.post(reverse('lab-10:add_watch_later', kwargs={'id': 'tt1981128'}))
        self.assertEqual(response.status_code, 302)

    def test_add_watch_later_case3(self):
        response = self.client.post(reverse('lab-10:add_watch_later', kwargs={'id': 'tt1981128'}))
        self.assertEqual(response.status_code, 302)

    def test_add_watch_later_case4(self):
        response = self.client.post(reverse('lab-10:add_watch_later', kwargs={'id': 'tt1981128'}))
        response = self.client.post(reverse('lab-10:add_watch_later', kwargs={'id': 'tt1981128'}))
        self.assertEqual(response.status_code, 302)

    def test_movie_list(self):
        response = self.client.post('/lab-10/movie/list/')
        self.assertEqual(response.status_code, 200)

    def test_movie_detail_case1(self):
        response = self.client.post(reverse('lab-10:movie_detail', kwargs={'id': 'tt1981128'}))
        html_response = response.content.decode('utf8')
        self.assertIn("Geostorm", html_response)

    def test_movie_detail_case2(self):
        session = self.client.session
        session['user_login'] = 'arga.ghulam'
        session['kode_identitas'] = '1606821601'
        session.save()

        response = self.client.post(reverse('lab-10:movie_detail', kwargs={'id': 'tt1981128'}))
        html_response = response.content.decode('utf8')
        self.assertIn("Geostorm", html_response)

    def test_api_search_movie_case1(self):
        session = self.client.session
        session['user_login'] = 'arga.ghulam'
        session['kode_identitas'] = '1606821601'
        session.save()

        response_post = self.client.post(reverse('lab-10:api_search_movie', kwargs={'judul': '6 Days', 'tahun': '2017'}))
        self.assertEqual(response_post.status_code, 200)

    def test_api_search_movie_case2(self):
        session = self.client.session
        session['user_login'] = 'arga.ghulam'
        session['kode_identitas'] = '1606821601'
        session.save()

        response_post = self.client.post(reverse('lab-10:api_search_movie', kwargs={'judul': '-', 'tahun': '-'}))
        self.assertEqual(response_post.status_code, 200)

    def test_list_watch_later_case1(self):
        response_post = self.client.post(reverse('lab-10:list_watch_later'))
        self.assertEqual(response_post.status_code, 200)

    def test_list_watch_later_case2(self):
        session = self.client.session
        session['user_login'] = 'arga.ghulam'
        session['kode_identitas'] = '1606821601'
        session['role'] = 'mahasiswa'
        session.save()

        response_post = self.client.post(reverse('lab-10:list_watch_later'))
        self.assertEqual(response_post.status_code, 200)

