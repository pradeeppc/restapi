# Generated by Django 2.1.1 on 2018-11-01 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0002_auto_20181101_0510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='imdb_score',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='movie',
            name='popularity',
            field=models.FloatField(blank=True, null=True),
        ),
    ]