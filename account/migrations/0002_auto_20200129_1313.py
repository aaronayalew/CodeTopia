# Generated by Django 3.0.2 on 2020-01-29 21:13

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(upload_to=account.models.get_profile_pic_path, verbose_name='Profile Picture'),
        ),
    ]
