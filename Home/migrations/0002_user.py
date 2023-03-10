# Generated by Django 4.1.6 on 2023-03-10 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('bio', models.CharField(max_length=100)),
                ('born', models.DateField()),
                ('date_of_singup', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
