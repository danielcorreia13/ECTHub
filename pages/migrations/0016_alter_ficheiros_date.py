# Generated by Django 3.2.3 on 2021-06-01 22:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_alter_ficheiros_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficheiros',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 1, 22, 11, 7, 167487)),
        ),
    ]