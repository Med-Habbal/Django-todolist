# Generated by Django 3.1.5 on 2021-02-04 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TacheLongCours', '0010_auto_20210204_0843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.AddField(
            model_name='typedetache',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
