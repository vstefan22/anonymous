# Generated by Django 4.1.7 on 2023-08-13 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anonymous', '0012_messages_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comments',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]