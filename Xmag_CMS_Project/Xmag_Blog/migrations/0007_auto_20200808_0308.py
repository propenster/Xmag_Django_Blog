# Generated by Django 3.1 on 2020-08-08 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Xmag_Blog', '0006_auto_20200808_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Xmag_Blog.category'),
        ),
    ]
