# Generated by Django 4.0 on 2022-09-02 14:05

import autoslug.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvt', '0002_alter_posts_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='publish',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 2, 19, 35, 7, 634412)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, max_length=250, null=True, populate_from=models.CharField(max_length=300), unique=True),
        ),
    ]
