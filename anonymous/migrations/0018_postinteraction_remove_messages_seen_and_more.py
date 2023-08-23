# Generated by Django 4.1.7 on 2023-08-16 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anonymous', '0017_messages_seen'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostInteraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='messages',
            name='seen',
        ),
        migrations.AddField(
            model_name='post',
            name='post_interaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='anonymous.postinteraction'),
        ),
    ]
