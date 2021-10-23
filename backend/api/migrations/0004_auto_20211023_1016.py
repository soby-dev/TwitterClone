# Generated by Django 3.2.8 on 2021-10-23 10:16

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_tweet_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='id',
        ),
        migrations.AddField(
            model_name='tweet',
            name='code',
            field=models.CharField(default=api.models.Tweet.event_code, max_length=25, primary_key=True, serialize=False),
        ),
    ]
