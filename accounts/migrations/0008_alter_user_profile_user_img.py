# Generated by Django 4.2 on 2023-04-16 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_user_profile_user_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='user_img',
            field=models.ImageField(blank=True, null=True, upload_to='profile_img'),
        ),
    ]