# Generated by Django 2.0 on 2018-01-22 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seekersdetail',
            name='Gender',
        ),
        migrations.RemoveField(
            model_name='seekersdetail',
            name='address',
        ),
    ]
