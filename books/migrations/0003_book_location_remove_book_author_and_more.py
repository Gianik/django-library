# Generated by Django 4.1.3 on 2022-11-08 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='location',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Exactus Office'), (2, 'Owner’s Home'), (3, 'In the Matrix')], default=1),
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AlterField(
            model_name='book',
            name='checked_out_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_borrower', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='book',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('AV', 'Available'), ('CO', 'Checked_out'), ('DA', 'Damaged'), ('LO', 'Lost')], default='AV', max_length=2),
        ),
        migrations.AlterField(
            model_name='book',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Hardcover'), (2, 'Paperback'), (3, 'Digital Copy')], default=1),
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(related_name='book_authors', to=settings.AUTH_USER_MODEL),
        ),
    ]
