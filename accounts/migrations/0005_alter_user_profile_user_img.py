# Generated by Django 4.2 on 2023-04-16 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_profile_user_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='user_img',
            field=models.ImageField(default='profile_img\\user_default.png', upload_to='profile_img'),
        ),
    ]