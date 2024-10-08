# Generated by Django 5.0.7 on 2024-08-30 09:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='seller',
        ),
        migrations.AddField(
            model_name='dog',
            name='display_img',
            field=models.FileField(default='', upload_to='dog_display_img'),
        ),
        migrations.AddField(
            model_name='dog',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default='PENDING', max_length=10),
        ),
    ]
