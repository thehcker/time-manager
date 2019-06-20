# Generated by Django 2.2.2 on 2019-06-20 22:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0010_album_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
