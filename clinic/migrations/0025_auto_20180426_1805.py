# Generated by Django 2.0.4 on 2018-04-26 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0024_auto_20180425_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='fichetechnique',
            name='echo_abdo',
            field=models.TextField(blank=True, verbose_name='échographie abdominale'),
        ),
        migrations.AddField(
            model_name='fichetechnique',
            name='kaliemia',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, verbose_name='kaliémie meq/l'),
        ),
        migrations.AddField(
            model_name='fichetechnique',
            name='natremia',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True, verbose_name='natrémie meq/l'),
        ),
        migrations.AlterField(
            model_name='fichetechnique',
            name='cholesterol',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, verbose_name='choletérol total'),
        ),
        migrations.AlterField(
            model_name='fichetechnique',
            name='glycemia',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='glycémie g/l'),
        ),
        migrations.AlterField(
            model_name='fichetechnique',
            name='hdl',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, verbose_name='HDL'),
        ),
        migrations.AlterField(
            model_name='fichetechnique',
            name='hemoglobin',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='hémoglobinémie (g/dl)'),
        ),
        migrations.AlterField(
            model_name='fichetechnique',
            name='ldl',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, verbose_name='LDL'),
        ),
        migrations.AlterField(
            model_name='fichetechnique',
            name='triglyceride',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, verbose_name='triglycérides'),
        ),
    ]
