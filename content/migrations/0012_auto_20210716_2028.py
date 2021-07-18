# Generated by Django 3.2.4 on 2021-07-16 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0011_content_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='intro',
            field=models.CharField(default='loremipsum', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='content',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='contentmeta',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]