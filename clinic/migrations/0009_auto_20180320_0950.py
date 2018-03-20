# Generated by Django 2.0.3 on 2018-03-20 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0008_auto_20180309_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultation',
            name='med_ref',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Médecin réfferent'),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='auscultation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
