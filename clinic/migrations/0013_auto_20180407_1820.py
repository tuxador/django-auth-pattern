# Generated by Django 2.0.3 on 2018-04-07 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0012_auto_20180407_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fichetechnique',
            name='clearance_cr',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Fonction rénale (clearance)'),
        ),
        migrations.AlterField(
            model_name='fichetechnique',
            name='dfg',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Fonction rénale (Débit de filtration glomérulaire)'),
        ),
        migrations.AlterField(
            model_name='fichetechnique',
            name='echocoeur',
            field=models.TextField(blank=True, verbose_name='Echocoeur (conclusion)'),
        ),
    ]
