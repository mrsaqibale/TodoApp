# Generated by Django 5.0.2 on 2024-03-03 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbtodo',
            name='tdIsDeleted',
            field=models.BooleanField(default=False),
        ),
    ]
