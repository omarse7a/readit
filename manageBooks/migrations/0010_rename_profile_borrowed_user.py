# Generated by Django 5.0.6 on 2024-05-23 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manageBooks', '0009_alter_borrowed_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrowed',
            old_name='profile',
            new_name='user',
        ),
    ]
