# Generated by Django 5.0.1 on 2024-01-03 10:16

import django.db.models.deletion
import sns.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='list',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to=sns.models.media_save_path),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='quote_tweet_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quote', to='sns.tweet'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='reply_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='sns.tweet'),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.CharField(blank=True, max_length=160),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to=sns.models.media_save_path),
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=sns.models.media_save_path),
        ),
        migrations.AlterField(
            model_name='user',
            name='website',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
