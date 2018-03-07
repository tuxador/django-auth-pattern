# Generated by Django 2.0.3 on 2018-03-07 19:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_auto_20180307_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convention',
            name='date_depot',
            field=models.DateField(default=datetime.datetime(2018, 3, 7, 19, 49, 3, 195037, tzinfo=utc), verbose_name='date du depôt du dossier'),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='code',
            field=models.CharField(max_length=15, verbose_name='Code'),
        ),
    ]
