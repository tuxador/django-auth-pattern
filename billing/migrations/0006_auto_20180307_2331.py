# Generated by Django 2.0.3 on 2018-03-07 22:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0005_auto_20180307_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convention',
            name='date_depot',
            field=models.DateField(default=datetime.datetime(2018, 3, 7, 22, 31, 26, 919178, tzinfo=utc), verbose_name='date du depôt du dossier'),
        ),
    ]
