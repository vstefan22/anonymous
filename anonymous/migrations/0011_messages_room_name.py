# Generated by Django 4.1.7 on 2023-08-10 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anonymous', '0010_remove_messages_user_receiver_request_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='room_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
