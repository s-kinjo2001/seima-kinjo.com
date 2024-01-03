# Generated by Django 5.0.1 on 2024-01-03 13:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0004_alter_tweet_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='retweet',
            name='retweeted_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
