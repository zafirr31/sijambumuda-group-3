from django.test import TestCase

class DataPage(TestCase):

    def test_data_page(self):
        time = datetime.datetime.now()
        peminjaman = Peminjaman.objects.create(
                book_title = "Test Title",
                borrower_name = "Test Name",
                borrow_time = time,
            )
        response = Client().get('/datapeminjaman/')
        self.assertIn("Judul Buku: Test Title; Peminjam: Test Name; Tanggal Peminjaman: " + time.strftime("%B %d, %Y") + " WIB", response.content.decode('utf-8'))


    def test_data_page_add(self):
        before = Peminjaman.objects.all().count()
        Peminjaman.objects.create(
                book_title = "Test Title",
                borrower_name = "Test Name",
                borrow_time = datetime.datetime.now()
            )
        after = Peminjaman.objects.all().count()
        self.assertEqual(before + 1, after)
