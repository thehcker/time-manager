# Generated by Django 2.2 on 2019-05-07 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20190507_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='audio_file',
            field=models.CharField(max_length=200),
        ),
    ]
