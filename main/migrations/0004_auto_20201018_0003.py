# Generated by Django 3.1.2 on 2020-10-17 17:03

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201015_1522'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': 'Bình luận'},
        ),
        migrations.AlterField(
            model_name='news',
            name='detail',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
