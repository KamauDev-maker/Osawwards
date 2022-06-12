# Generated by Django 4.0.5 on 2022-06-11 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='content_average',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='rating',
            name='design_average',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='rating',
            name='usability_average',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
