from django.test import TestCase
from django.test import Client
from django.urls import resolve
from django.http import HttpRequest
from .views import show_history, history_json, profile
from django.contrib.auth.models import User

class HistoryPinjamTest(TestCase):

    def test_history_url_no_login(self):
        response = Client().get('/history/')
        self.assertEqual(response.status_code, 302)

    # def test_history_url_login(self):
    #     user = User.objects.create_user(username='jahns')
    #     user.set_password("1234Aaa.")
    #     user.save()
    #     client = Client()
    #     logged_in = client.login(username='jahns', password='1234Aaa.')
    #     response = Client().get('/history/')
    #     self.assertEqual(response.status_code, 200)

    def test_history_fungsi_show_history(self):
        found = resolve('/history/')
        self.assertEqual(found.func, show_history)

    # def test_history_isi_html(self):
    #     user = User.objects.create_user(username='jahns')
    #     user.set_password("1234Aaa.")
    #     user.save()
    #     client = Client()
    #     logged_in = client.login(username='jahns', password='1234Aaa.')
    #     request = HttpRequest()
    #     response = show_history(request)
    #     html_response = response.content.decode('utf8')
    #     self.assertIn('Profile', html_response)

    def test_history_json_url_no_login(self):
        response = Client().get('/history/json/')
        self.assertEqual(response.status_code, 302)

    def test_history_json_fungsi_show_history(self):
        found = resolve('/history/json/')
        self.assertEqual(found.func, history_json)

    # def test_history_json_url_login(self):
    #     user = User.objects.create_user(username='jahns')
    #     user.set_password("1234Aaa.")
    #     user.save
    #     client = Client()
    #     logged_in = client.login(username='jahns', password='1234Aaa.')
    #     response = Client().get('/history/json/')
    #     self.assertEqual(response.status_code, 200)

    # def test_history_json_isi_html(self):
    #     user = User.objects.create_user(username='jahns')
    #     user.set_password("1234Aaa.")
    #     user.save()
    #     client = Client()
    #     logged_in = client.login(username='jahns', password='1234Aaa.')
    #     request = HttpRequest()
    #     response = history_json(request)
    #     html_response = response.content.decode('utf8')
    #     self.assertIn('[', html_response)