# Generated by Django 2.0.3 on 2018-03-09 07:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0011_auto_20180309_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convention',
            name='date_depot',
            field=models.DateField(default=datetime.datetime(2018, 3, 9, 7, 24, 25, 340939, tzinfo=utc), verbose_name='date depôt dossier'),
        ),
    ]
