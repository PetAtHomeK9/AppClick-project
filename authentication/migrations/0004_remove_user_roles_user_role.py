# Generated by Django 5.0.7 on 2024-09-22 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_user_roles_alter_user_profile_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='roles',
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('seller', 'Seller'), ('buyer', 'Buyer')], default='seller', max_length=10),
        ),
    ]
