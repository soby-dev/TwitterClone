# Generated by Django 3.2.8 on 2021-10-23 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='dateTimeCreated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
