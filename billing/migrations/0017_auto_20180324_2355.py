# Generated by Django 2.0.3 on 2018-03-24 22:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0016_auto_20180323_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convention',
            name='date_depot',
            field=models.DateField(default=datetime.datetime(2018, 3, 24, 22, 55, 32, 257803, tzinfo=utc), verbose_name='date depôt dossier'),
        ),
    ]
