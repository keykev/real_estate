# Generated by Django 3.1.1 on 2020-10-04 20:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20201001_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 4, 13, 45, 43, 660385)),
        ),
    ]
