# Generated by Django 5.0.6 on 2024-05-22 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manageBooks', '0006_book_current_borrower_alter_book_category_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='borrowed',
            options={'verbose_name': 'borrowed book'},
        ),
        migrations.RenameField(
            model_name='borrowed',
            old_name='user',
            new_name='profile',
        ),
    ]