# Generated by Django 2.1.1 on 2019-03-22 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PinjamModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('nomor_buku', models.IntegerField()),
                ('tanggal_pinjam', models.DateField(auto_now_add=True)),
                ('nama_peminjam', models.CharField(max_length=100)),
                ('buku_dipinjam', models.CharField(max_length=100)),
            ],
        ),
    ]
