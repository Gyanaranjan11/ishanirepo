# Generated by Django 2.2.11 on 2021-04-18 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0003_auto_20210409_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='dob',
            field=models.DateTimeField(blank=True, max_length=50, null=True),
        ),
    ]
