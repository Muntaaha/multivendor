# Generated by Django 3.0.6 on 2020-06-17 17:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20200615_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='date_added',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 17, 17, 58, 32, 442131)),
        ),
    ]
