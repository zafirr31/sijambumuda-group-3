# Generated by Django 2.1.1 on 2019-04-27 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_anggota', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='member',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='nomor_identitas',
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='alamat_rumah',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
