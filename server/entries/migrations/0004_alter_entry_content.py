# Generated by Django 4.2 on 2023-04-28 10:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0003_alter_entry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
