from django.test import TestCase
from django.test import Client
from django.urls import resolve
from django.http import HttpRequest

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
        form = PinjamForm(data={'nomor_buku':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['nomor_buku'],
            ['This field is required.']
        )
        
    def test_form(self):
        dummy_member = Member.objects.create(
            Nama = "Shafiya",
            Nomor_Identitas = "1806235845",
            Username = "shafiya123",
            Email = "2019-03-25",
            Password = "adzhani",
            Alamat_Rumah = "Depok"
        )
        response = Client().post('/form-pinjam/',{'username':'shafiya123'})
        self.assertIn("</form>",response.content.decode())