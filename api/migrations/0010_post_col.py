# Generated by Django 3.2.6 on 2024-05-01 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_articlecomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='col',
            field=models.IntegerField(default=1),
        ),
    ]
