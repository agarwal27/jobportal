# Generated by Django 2.0 on 2018-01-23 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20180123_0941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seekersdetail',
            name='City',
        ),
        migrations.RemoveField(
            model_name='seekersdetail',
            name='College_name',
        ),
        migrations.RemoveField(
            model_name='seekersdetail',
            name='Graduation_percent',
        ),
        migrations.RemoveField(
            model_name='seekersdetail',
            name='Mobile_Number',
        ),
        migrations.RemoveField(
            model_name='seekersdetail',
            name='Stream',
        ),
        migrations.RemoveField(
            model_name='seekersdetail',
            name='secondary_board',
        ),
        migrations.RemoveField(
            model_name='seekersdetail',
            name='secondary_percent',
        ),
        migrations.RemoveField(
            model_name='seekersdetail',
            name='senior_board',
        ),
        migrations.RemoveField(
            model_name='seekersdetail',
            name='senior_percent',
        ),
    ]
