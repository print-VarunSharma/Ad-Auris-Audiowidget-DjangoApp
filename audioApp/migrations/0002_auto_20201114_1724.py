# Generated by Django 3.1.3 on 2020-11-15 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audioApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='narration',
            name='narration_editor',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='company_name',
        ),
        migrations.AddField(
            model_name='narration',
            name='file',
            field=models.FileField(default=None, upload_to='media/'),
        ),
    ]