# Generated by Django 3.2.4 on 2021-07-16 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth1', '0006_auto_20210715_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='userrole',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
