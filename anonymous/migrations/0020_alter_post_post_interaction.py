# Generated by Django 4.1.7 on 2023-08-16 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anonymous', '0019_postinteraction_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_interaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='interaction', to='anonymous.postinteraction'),
        ),
    ]
