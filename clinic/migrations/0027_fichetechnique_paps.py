# Generated by Django 2.0.4 on 2018-04-26 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0026_auto_20180426_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='fichetechnique',
            name='paps',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='PAPS'),
        ),
    ]