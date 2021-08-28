# Generated by Django 3.2.4 on 2021-07-04 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_rename_status_comment_status_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentmeta',
            name='content',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='content_meta', to='content.content'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contentmeta',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_meta', to='content.postcategory'),
        ),
    ]
