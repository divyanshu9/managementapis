# Generated by Django 3.2.6 on 2021-08-29 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth1', '0010_auto_20210828_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='contact',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='userdetail',
            name='email',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
