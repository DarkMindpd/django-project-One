# Generated by Django 4.2 on 2023-04-11 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('Home', '0011_alter_user_profile_bio_alter_user_profile_born'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user_profile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user_profile'),
        ),
        migrations.DeleteModel(
            name='User_profile',
        ),
    ]
