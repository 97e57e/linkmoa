# Generated by Django 2.1.7 on 2019-08-01 10:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkmoa', '0011_auto_20190730_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memo',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 1, 10, 4, 14, 894117), verbose_name='date_published'),
        ),
    ]
