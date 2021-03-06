# Generated by Django 2.0.4 on 2018-04-26 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0025_auto_20180426_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fichetechnique',
            name='quotation1',
            field=models.ManyToManyField(blank=True, related_name='q1', to='billing.Quotation'),
        ),
        migrations.AlterField(
            model_name='fichetechnique',
            name='quotation2',
            field=models.ManyToManyField(blank=True, related_name='q2', to='billing.Quotation'),
        ),
        migrations.AlterField(
            model_name='fichetechnique',
            name='quotation3',
            field=models.ManyToManyField(blank=True, related_name='q3', to='billing.Quotation'),
        ),
    ]
