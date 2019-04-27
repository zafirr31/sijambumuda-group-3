from django.test import TestCase, Client
from django.urls import resolve
from django.http import HttpRequest

from .models import Testimoni
from .views import *
import datetime



class AboutDanTestimoni(TestCase):
    def test_AboutDanTestimoni_url_ada(self):
        response = Client().get('/about-dan-testimoni/')
        self.assertEqual(response.status_code, 200)

    def test_AboutDanTestimoni_fungsi_renderpage(self):
        found = resolve('/about-dan-testimoni/')
        self.assertEqual(found.func, about)

    def test_AboutDanTestimoni_isi_html(self):
        request = HttpRequest()
        response = about(request)
        html_response = response.content.decode('utf8')
        self.assertIn('Tentang SijambuMuda', html_response)

    def test_AboutDanTestimoni_model(self):
        time = datetime.datetime.now()
        testMember = Testimoni.objects.create(
        Username  = "somedude",
        Pesan = "website ini keren",
        Tanggal_Pesan = time,
        )

        jumlah_testimoni = Testimoni.objects.all().count()
        self.assertEqual(jumlah_testimoni, 1 )

    class ConfigTest(TestCase):
        def test_apps(self):
            self.assertEqual(AboutDanTestimoniConfig.name, 'About_dan_Testimoni')
            self.assertEqual(apps.get_app_config('About_dan_Testimoni').name, 'About_dan_Testimoni')




# Create your tests here.
