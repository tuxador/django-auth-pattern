# Generated by Django 2.0.4 on 2018-04-26 17:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('correspondence', '0027_auto_20180426_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arret',
            name='arret_date',
            field=models.DateField(default=datetime.datetime(2018, 4, 26, 17, 6, 52, 246435, tzinfo=utc), verbose_name='Date du début'),
        ),
        migrations.AlterField(
            model_name='arret',
            name='redaction_date',
            field=models.DateField(default=datetime.datetime(2018, 4, 26, 17, 6, 52, 246502, tzinfo=utc), verbose_name='délivré le'),
        ),
        migrations.AlterField(
            model_name='certificat',
            name='certificat_date',
            field=models.DateField(default=datetime.datetime(2018, 4, 26, 17, 6, 52, 244191, tzinfo=utc), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='courrier_date',
            field=models.DateField(default=datetime.datetime(2018, 4, 26, 17, 6, 52, 244931, tzinfo=utc), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='ordonnance',
            name='ordonnance_date',
            field=models.DateField(default=datetime.datetime(2018, 4, 26, 17, 6, 52, 242143, tzinfo=utc), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='stomato',
            name='stomato_date',
            field=models.DateField(default=datetime.datetime(2018, 4, 26, 17, 6, 52, 245579, tzinfo=utc), verbose_name='Date'),
        ),
    ]
