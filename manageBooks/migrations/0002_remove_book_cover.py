# Generated by Django 5.0.6 on 2024-05-14 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manageBooks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='cover',
        ),
    ]
