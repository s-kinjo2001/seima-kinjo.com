# Generated by Django 5.0.1 on 2024-01-03 10:25

import sns.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0003_alter_tweet_quote_tweet_id_alter_tweet_reply_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=sns.models.media_save_path),
        ),
    ]