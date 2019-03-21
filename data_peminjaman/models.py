from django.db import models

class Peminjaman(models.Model):

	book_title = models.CharField(
			max_length=100,
		)
	borrower_name = models.CharField(
			max_length=100,
		)
	borrow_time = models.DateField()