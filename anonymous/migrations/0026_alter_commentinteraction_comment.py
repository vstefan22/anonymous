# Generated by Django 4.1.7 on 2023-08-27 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anonymous', '0025_commentinteraction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentinteraction',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='interaction', to='anonymous.comments'),
        ),
    ]
