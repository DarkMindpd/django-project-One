# Generated by Django 4.2 on 2023-04-16 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_user_profile_user_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='user_img',
            field=models.ImageField(default='profile_img\\user_default.png', upload_to='profile_img'),
        ),
    ]
