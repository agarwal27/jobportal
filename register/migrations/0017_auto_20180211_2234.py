# Generated by Django 2.0 on 2018-02-11 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0016_recruitersdetail_company_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='seekersdetails',
            name='Photo',
            field=models.FileField(default=0, upload_to=''),
        ),
        migrations.AddField(
            model_name='seekersdetails',
            name='Resume',
            field=models.FileField(default=0, upload_to=''),
        ),
    ]
