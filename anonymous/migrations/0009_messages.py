# Generated by Django 4.1.7 on 2023-08-10 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anonymous', '0008_chat_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('user_receiver_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiverMessage', to='anonymous.anonymous')),
                ('user_sender_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='senderMessage', to='anonymous.anonymous')),
            ],
        ),
    ]
