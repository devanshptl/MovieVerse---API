# Generated by Django 5.0.6 on 2024-07-13 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='watch',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='watch',
            name='total_reviews',
            field=models.IntegerField(default=0),
        ),
    ]
