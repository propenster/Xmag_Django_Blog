# Generated by Django 3.1 on 2020-08-07 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Xmag_Blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='The title of the article',
            new_name='title',
        ),
    ]
