# Generated by Django 4.1.6 on 2023-02-24 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_img', models.URLField()),
                ('tag', models.CharField(max_length=15)),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('user_img', models.URLField()),
                ('user_name', models.CharField(max_length=30)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
