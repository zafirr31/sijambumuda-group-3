from django.test import TestCase
from django.test import Client
from django.urls import resolve
from django.http import HttpRequest
from landingpage.apps import LandingpageConfig
from django.apps import apps

from .views import *
from .models import *
import datetime

class LandingPage(TestCase):

    def test_landing_page_url_ada(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_landing_page_fungsi_index(self):
        found = resolve('/')
        self.assertEqual(found.func, index)
    
    def test_dummy_page(self):
        response = Client().get("/test")
        self.assertEqual(response.status_code,404)

class ConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(LandingpageConfig.name, 'landingpage')
        self.assertEqual(apps.get_app_config('landingpage').name, 'landingpage')