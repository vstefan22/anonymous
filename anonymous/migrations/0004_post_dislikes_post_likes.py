# Generated by Django 4.1.7 on 2023-04-08 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anonymous', '0003_delete_id_remove_anonymous_user_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
