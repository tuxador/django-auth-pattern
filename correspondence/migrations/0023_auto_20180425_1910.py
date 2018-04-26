# Generated by Django 2.0.4 on 2018-04-25 18:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('correspondence', '0022_auto_20180425_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arret',
            name='arret_date',
            field=models.DateField(default=datetime.datetime(2018, 4, 25, 18, 10, 29, 849752, tzinfo=utc), verbose_name='Date du début'),
        ),
        migrations.AlterField(
            model_name='arret',
            name='redaction_date',
            field=models.DateField(default=datetime.datetime(2018, 4, 25, 18, 10, 29, 849821, tzinfo=utc), verbose_name='délivré le'),
        ),
        migrations.AlterField(
            model_name='certificat',
            name='certificat_date',
            field=models.DateField(default=datetime.datetime(2018, 4, 25, 18, 10, 29, 847549, tzinfo=utc), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='courrier_date',
            field=models.DateField(default=datetime.datetime(2018, 4, 25, 18, 10, 29, 848227, tzinfo=utc), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='ordonnance',
            name='ordonnance_date',
            field=models.DateField(default=datetime.datetime(2018, 4, 25, 18, 10, 29, 845535, tzinfo=utc), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='stomato',
            name='stomato_date',
            field=models.DateField(default=datetime.datetime(2018, 4, 25, 18, 10, 29, 848923, tzinfo=utc), verbose_name='Date'),
        ),
    ]
