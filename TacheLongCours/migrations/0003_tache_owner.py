# Generated by Django 3.1.5 on 2021-02-03 08:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TacheLongCours', '0002_auto_20210203_0825'),
    ]

    operations = [
        migrations.AddField(
            model_name='tache',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Tache_oner', to='auth.user'),
            preserve_default=False,
        ),
    ]
