# Generated by Django 3.2.8 on 2021-10-27 06:12

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20211027_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
