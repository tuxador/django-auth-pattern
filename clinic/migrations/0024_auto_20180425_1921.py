# Generated by Django 2.0.4 on 2018-04-25 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0023_auto_20180425_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='birth_place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='originaires', to='clinic.Wilaya', verbose_name='lieu de naisssance'),
        ),
    ]
