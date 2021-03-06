# Generated by Django 2.0.3 on 2018-03-08 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0003_auto_20180307_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='reception',
            name='manque',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='montant manquant'),
        ),
        migrations.AddField(
            model_name='reception',
            name='paid',
            field=models.NullBooleanField(verbose_name='montant reglé'),
        ),
        migrations.AddField(
            model_name='reception',
            name='reduction',
            field=models.NullBooleanField(verbose_name='réduction'),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='ischaemia',
            field=models.CharField(blank=True, choices=[('N', 'Null'), ('S', 'Septal'), ('A', 'Anterior'), ('L', 'Lateral'), ('P', 'Posterior')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='lesion',
            field=models.CharField(blank=True, choices=[('N', 'Null'), ('S', 'Septal'), ('A', 'Anterior'), ('L', 'Lateral'), ('P', 'Posterior')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='necrosis',
            field=models.CharField(blank=True, choices=[('N', 'Null'), ('S', 'Septal'), ('A', 'Anterior'), ('L', 'Lateral'), ('P', 'Posterior')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='rythm',
            field=models.CharField(blank=True, choices=[('S', 'Sinusal'), ('F', 'Atrial Fibrillation'), ('R', 'Atrial Flutter'), ('P', 'Pace Maker'), ('T', 'TV')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='t_inversion',
            field=models.CharField(blank=True, choices=[('N', 'Null'), ('S', 'Septal'), ('A', 'Anterior'), ('L', 'Lateral'), ('P', 'Posterior')], max_length=1, null=True),
        ),
    ]
