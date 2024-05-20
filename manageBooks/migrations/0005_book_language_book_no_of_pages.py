# Generated by Django 5.0.6 on 2024-05-16 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageBooks', '0004_alter_book_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.CharField(default='en', max_length=100),
        ),
        migrations.AddField(
            model_name='book',
            name='no_of_pages',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
