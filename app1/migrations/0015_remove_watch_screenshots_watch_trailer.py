# Generated by Django 5.0.6 on 2024-07-22 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_watch_screenshots'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watch',
            name='screenshots',
        ),
        migrations.AddField(
            model_name='watch',
            name='trailer',
            field=models.URLField(blank=True, null=True),
        ),
    ]
