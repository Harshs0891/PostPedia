# Generated by Django 5.0.7 on 2024-07-16 15:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to='blogapp.category'),
        ),
        migrations.AddField(
            model_name='blog',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
