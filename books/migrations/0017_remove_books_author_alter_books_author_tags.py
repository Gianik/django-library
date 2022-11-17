# Generated by Django 4.1.3 on 2022-11-16 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0016_authors_remove_books_tags_books_author_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='author',
        ),
        migrations.AlterField(
            model_name='books',
            name='author_tags',
            field=models.ManyToManyField(blank=True, to='books.authors'),
        ),
    ]