# Generated by Django 2.1.1 on 2018-10-31 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('imdb_score', models.FloatField(default=0.0)),
                ('popularity', models.FloatField(blank=True, null=True)),
                ('movie_id', models.CharField(max_length=30)),
                ('genres', models.CharField(max_length=120)),
                ('director', models.CharField(max_length=100)),
            ],
        ),
    ]