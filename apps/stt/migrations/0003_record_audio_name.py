# Generated by Django 4.1.3 on 2022-11-14 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stt', '0002_alter_record_options_alter_record_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='audio_name',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
    ]