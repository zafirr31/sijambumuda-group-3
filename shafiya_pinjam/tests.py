from django.test import TestCase
from django.test import Client
from django.urls import resolve
from django.http import HttpRequest
from shafiya_pinjam.apps import ShafiyaPinjamConfig
from django.apps import apps

from .views import *
from .models import PinjamModel
from .forms import PinjamForm
from form_anggota.models import Member
import datetime

class SampleTest(TestCase):
    # test eksistensi page form pinjam
    def test_page_form_pinjam(self):
        response = Client().get('/form-pinjam/')
        self.assertEqual(response.status_code,200)

    def test_form_pinjam_using_index_func(self):
        found = resolve('/form-pinjam/')
        self.assertEqual(found.func, pinjam)

    def test_status_template_form_pinjam_used(self):
        response = Client().get('/form-pinjam/')
        self.assertTemplateUsed(response, 'page/form-pinjam.html')

    # test untuk model
    def test_pinjam_models_created(self):
        time = datetime.datetime.now()
        dummy_pinjam = PinjamModel.objects.create(
            username = "shafiya123",
            email = "shafiya123@gmail.com",
            nomor_buku = "1",
            tanggal_pinjam = time,
        )
        total_pinjam = PinjamModel.objects.all().count()
        self.assertEqual(total_pinjam, 1)
    
    def test_formusername_validated(self):
        form = PinjamForm(data={'username':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['username'],
            ['This field is required.']
        )

    def test_formemail_validated(self):
        form = PinjamForm(data={'email':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['email'],
            ['This field is required.']
        )

    def test_formnobuku_validated(self):
        form = PinjamForm(data={'nomor_buku': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['nomor_buku'],
            ['This field is required.']
        )
        
    def test_form(self):
        time = datetime.datetime.now()
        buku = Buku.objects.create(
            nomor_buku = 1,
            judul_buku = "Test Judul",
            pengarang = "Test Pengarang",
            kategori = "Test Kategori",
            penerbit = "Test Penerbit",
            sinopsis = "Test Sinopsis",
        )
        member = Member.objects.create(
            Nama = "Test Nama",
            Nomor_Identitas = 31,
            Username = "test",
            Email = "test@test.com",
            Password = "Test Password",
            Alamat_Rumah = "Test Alamat",
        )
        Client().post('/form-pinjam/', {"username": "test", "email": "test@test.com", "nomor_buku": 1})
        response1 = Client().get('/datapeminjaman/')
        self.assertIn("<b>Judul Buku:</b> Test Judul; <b>Peminjam:</b> Test Nama; <b>Tanggal Peminjaman:</b> " + time.strftime("%B %d, %Y"), response1.content.decode('utf-8'))

    def test_buku_doesnt_exist(self):
        member = Member.objects.create(
            Nama = "Test Nama",
            Nomor_Identitas = 31,
            Username = "test",
            Email = "test@test.com",
            Password = "Test Password",
            Alamat_Rumah = "Test Alamat",
        )
        response = Client().post("/form-pinjam/", {"username": "test", "email": "test@test.com", "nomor_buku": "1"})
        self.assertIn("Buku tidak ada", response.content.decode('utf-8'))

    def test_member_doesnt_exist(self):
        response = Client().post("/form-pinjam/", {"username": "test", "email": "test@test.com", "nomor_buku": "1"})
        self.assertIn("Username tidak ada", response.content.decode('utf-8'))

class ConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(ShafiyaPinjamConfig.name, 'shafiya_pinjam')
        self.assertEqual(apps.get_app_config('shafiya_pinjam').name, 'shafiya_pinjam')