# Generated by Django 3.1 on 2021-08-25 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_quote_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='title',
            field=models.CharField(default='invoicetitle', max_length=250),
            preserve_default=False,
        ),
    ]
