# Generated by Django 4.2 on 2023-07-05 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='theme',
            old_name='author',
            new_name='author_id',
        ),
    ]