# Generated by Django 2.1.1 on 2019-03-21 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shafiya_pinjam', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pinjammodel',
            name='tanggal_pinjam',
            field=models.DateField(auto_now_add=True),
        ),
    ]