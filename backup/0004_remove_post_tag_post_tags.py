# Generated by Django 4.2 on 2023-04-30 06:20

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('post', '0003_rename_user_name_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tag',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]