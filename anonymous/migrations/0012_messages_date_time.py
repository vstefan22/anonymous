# Generated by Django 4.1.7 on 2023-08-10 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anonymous', '0011_messages_room_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
