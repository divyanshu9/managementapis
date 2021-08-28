# Generated by Django 3.2.4 on 2021-07-16 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0006_auto_20210715_0701'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='intro',
            field=models.CharField(default='Loremipsum', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='response',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='survey',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='surveyresponse',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
