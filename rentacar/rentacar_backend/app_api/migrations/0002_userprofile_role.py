# Generated by Django 4.0.5 on 2022-06-07 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.CharField(max_length=55, null=True),
        ),
    ]