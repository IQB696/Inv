# Generated by Django 4.2.1 on 2023-05-30 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='title',
            field=models.CharField(default='No title', max_length=256),
        ),
    ]
