# Generated by Django 4.1.6 on 2023-03-10 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_user_alter_comment_user_name_alter_post_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='user_name',
            field=models.CharField(max_length=30),
        ),
    ]
