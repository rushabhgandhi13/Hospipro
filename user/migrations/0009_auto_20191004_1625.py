# Generated by Django 2.2.5 on 2019-10-04 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_patient_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='slug',
        ),
        migrations.AddField(
            model_name='patient',
            name='allergy',
            field=models.CharField(default='water', max_length=200),
        ),
        migrations.AddField(
            model_name='patient',
            name='bloodgroup',
            field=models.CharField(default='B-negative', max_length=10),
        ),
        migrations.AddField(
            model_name='patient',
            name='diseases',
            field=models.CharField(default='cancer', max_length=200),
        ),
        migrations.AddField(
            model_name='patient',
            name='medihistory',
            field=models.CharField(default='medi history', max_length=200),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(max_length=250),
        ),
    ]