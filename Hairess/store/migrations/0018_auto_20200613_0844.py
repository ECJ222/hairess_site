# Generated by Django 3.0.6 on 2020-06-13 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_auto_20200612_1815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
    ]
