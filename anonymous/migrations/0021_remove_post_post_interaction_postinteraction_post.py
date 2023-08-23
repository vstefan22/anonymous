# Generated by Django 4.1.7 on 2023-08-23 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anonymous', '0020_alter_post_post_interaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_interaction',
        ),
        migrations.AddField(
            model_name='postinteraction',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='anonymous.post'),
        ),
    ]
