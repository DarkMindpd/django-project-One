# Generated by Django 4.1.6 on 2023-03-10 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_remove_user_user_pass'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
