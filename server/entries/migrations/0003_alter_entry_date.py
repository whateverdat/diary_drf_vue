# Generated by Django 4.2 on 2023-04-24 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0002_entry_location_alter_entry_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
