# Generated by Django 2.0.3 on 2018-04-07 17:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0019_auto_20180407_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convention',
            name='date_depot',
            field=models.DateField(default=datetime.datetime(2018, 4, 7, 17, 20, 22, 547501, tzinfo=utc), verbose_name='date depôt dossier'),
        ),
    ]
