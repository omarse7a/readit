# Generated by Django 4.2.13 on 2024-05-25 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageBooks', '0012_alter_book_copies'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='ratings',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
        ),
        migrations.AddField(
            model_name='book',
            name='reviews',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('Any', 'Any'), ('Adventure', 'Adventure'), ('Science fiction', 'Science fiction'), ('Thriller', 'Thriller'), ('Mystery', 'Mystery'), ('Horror', 'Horror'), ('Autobiographical', 'Autobiographical'), ('Fantasy', 'Fantasy'), ('Drama', 'Drama'), ('History', 'History'), ('Science', 'Science'), ('Romance', 'Romance'), ('Fiction', 'Fiction'), ('Dystopian', 'Dystopian')], default='Any', max_length=50),
        ),
    ]
