# Generated by Django 5.0.6 on 2024-05-23 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageBooks', '0011_book_borrowed_copies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='copies',
            field=models.IntegerField(default=1),
        ),
    ]
