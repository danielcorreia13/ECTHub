# Generated by Django 3.2.3 on 2021-05-31 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_assubdject'),
    ]

    operations = [
        migrations.AddField(
            model_name='ficheiros',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]