# Generated by Django 4.2.9 on 2024-09-05 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_remove_smile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.CharField(max_length=25000),
        ),
    ]
