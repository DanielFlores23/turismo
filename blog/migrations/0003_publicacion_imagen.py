# Generated by Django 3.1 on 2020-09-24 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200923_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]