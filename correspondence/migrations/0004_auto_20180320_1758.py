# Generated by Django 2.0.3 on 2018-03-20 16:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('correspondence', '0003_auto_20180320_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arret',
            name='arret_date',
            field=models.DateField(default=datetime.datetime(2018, 3, 20, 16, 58, 42, 623398, tzinfo=utc), verbose_name='Date du début'),
        ),
        migrations.AlterField(
            model_name='arret',
            name='redaction_date',
            field=models.DateField(default=datetime.datetime(2018, 3, 20, 16, 58, 42, 623510, tzinfo=utc), verbose_name='délivré le'),
        ),
        migrations.AlterField(
            model_name='certificat',
            name='certificat_date',
            field=models.DateField(default=datetime.datetime(2018, 3, 20, 16, 58, 42, 619966, tzinfo=utc), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='courrier_date',
            field=models.DateField(default=datetime.datetime(2018, 3, 20, 16, 58, 42, 621070, tzinfo=utc), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='ordonnance',
            name='ordonnance_date',
            field=models.DateField(default=datetime.datetime(2018, 3, 20, 16, 58, 42, 617083, tzinfo=utc), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='stomato',
            name='stomato_date',
            field=models.DateField(default=datetime.datetime(2018, 3, 20, 16, 58, 42, 622109, tzinfo=utc), verbose_name='Date'),
        ),
    ]