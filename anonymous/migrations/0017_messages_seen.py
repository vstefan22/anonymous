# Generated by Django 4.1.7 on 2023-08-16 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anonymous', '0016_remove_messages_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='seen',
            field=models.BooleanField(default=False),
        ),
    ]
