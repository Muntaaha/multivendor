# Generated by Django 3.0.6 on 2020-05-30 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20200529_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='password1',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='password2',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='username',
        ),
    ]