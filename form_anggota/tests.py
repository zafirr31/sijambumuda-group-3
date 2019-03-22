from django.test import TestCase
from django.test import Client
from django.urls import resolve
from django.http import HttpRequest
from form_anggota.apps import FormAnggotaConfig
from django.apps import apps

from .models import Member
from datetime import datetime
from .views import *

class FormAnggota(TestCase):
    def test_form_member_url_ada(self):
        response = Client().get('/registrasi-member/')
        self.assertEqual(response.status_code, 200)

    def test_form_member_fungsi_index(self):
        found = resolve('/registrasi-member/')
        self.assertEqual(found.func, registrasi_member)

    def test_form_member_isi_html(self):
        request = HttpRequest()
        response = registrasi_member(request)
        html_response = response.content.decode('utf8')
        self.assertIn('Registrasi Anggota', html_response)

    def test_poststatus_model_registrasi_member(self):
        testMember = Member.objects.create(
        Nama = "Rendya Yuschak",
        Nomor_Identitas = "1806205262",
        Username  = "Haskucy",
        Email = "rendyayuschak@gmail.com",
        Password = "siapatahu?",
        Alamat_Rumah = "Jalan Kotabaru no 15, Jakarta Pusat, Jakarta, 10150",
        )

        jumlahMember = Member.objects.all().count()
        self.assertEqual(jumlahMember, 1 )

    def test_username_already_exists(self):
        member = Member.objects.create(
            Nama = "Test Nama",
            Nomor_Identitas = 31,
            Username = "test",
            Email = "test@test.com",
            Password = "Test Password",
            Alamat_Rumah = "Test Alamat",
        )
        response = Client().post("/registrasi-member/", {"Nama": "Test Nama", "Nomor_Identitas": 31, "Username": "test", "Email": "test@test.com", "Password": "yayaya", "Alamat_Rumah": "Aceh"})
        self.assertIn("Username sudah terdaftar", response.content.decode('utf-8'))

    def test_create_user(self):
        self.form = DaftarMember(data={"Nama": "Test Nama", "Nomor_Identitas": 31, "Username": "test", "Email": "test@test.com", "Password": "yayaya", "Alamat_Rumah": "Aceh"})
        Client().post("/registrasi-member/", {"Nama": "Test Nama", "Nomor_Identitas": 31, "Username": "test", "Email": "test@test.com", "Password": "yayaya", "Alamat_Rumah": "Aceh"})
        self.assertTrue(self.form.is_valid)

class ConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(FormAnggotaConfig.name, 'form_anggota')
        self.assertEqual(apps.get_app_config('form_anggota').name, 'form_anggota')