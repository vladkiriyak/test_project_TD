# Generated by Django 3.0.7 on 2020-06-09 08:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.CharField(default=datetime.datetime(2020, 6, 9, 8, 10, 20, 775080), max_length=256),
        ),
    ]