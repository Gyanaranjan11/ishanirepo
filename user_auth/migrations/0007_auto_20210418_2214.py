# Generated by Django 2.2.11 on 2021-04-18 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0006_auto_20210418_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='created_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='modify_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
