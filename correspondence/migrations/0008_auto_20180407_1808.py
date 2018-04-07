# Generated by Django 2.0.3 on 2018-04-07 17:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('correspondence', '0007_auto_20180403_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arret',
            name='arret_date',
            field=models.DateField(default=datetime.datetime(2018, 4, 7, 17, 8, 35, 907312, tzinfo=utc), verbose_name='Date du début'),
        ),
        migrations.AlterField(
            model_name='arret',
            name='redaction_date',
            field=models.DateField(default=datetime.datetime(2018, 4, 7, 17, 8, 35, 907380, tzinfo=utc), verbose_name='délivré le'),
        ),
        migrations.AlterField(
            model_name='certificat',
            name='certificat_date',
            field=models.DateField(default=datetime.datetime(2018, 4, 7, 17, 8, 35, 905089, tzinfo=utc), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='courrier_date',
            field=models.DateField(default=datetime.datetime(2018, 4, 7, 17, 8, 35, 905781, tzinfo=utc), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='ordonnance',
            name='ordonnance_date',
            field=models.DateField(default=datetime.datetime(2018, 4, 7, 17, 8, 35, 903101, tzinfo=utc), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='stomato',
            name='stomato_date',
            field=models.DateField(default=datetime.datetime(2018, 4, 7, 17, 8, 35, 906404, tzinfo=utc), verbose_name='Date'),
        ),
    ]
