# Generated by Django 2.0.3 on 2018-03-20 08:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0013_auto_20180309_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convention',
            name='date_depot',
            field=models.DateField(default=datetime.datetime(2018, 3, 20, 8, 50, 6, 968711, tzinfo=utc), verbose_name='date depôt dossier'),
        ),
    ]
