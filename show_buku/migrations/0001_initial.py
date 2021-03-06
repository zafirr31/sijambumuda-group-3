# Generated by Django 2.1.1 on 2019-03-22 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buku',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomor_buku', models.IntegerField()),
                ('judul_buku', models.CharField(max_length=50)),
                ('pengarang', models.CharField(max_length=50)),
                ('kategori', models.CharField(max_length=50)),
                ('penerbit', models.CharField(max_length=50)),
                ('cover', models.ImageField(blank=True, upload_to='gallery')),
                ('sinopsis', models.TextField()),
            ],
        ),
    ]
