# Generated by Django 5.1.1 on 2024-10-27 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corduroyserver', '0004_trails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reports',
            name='approvalStatus',
            field=models.BooleanField(default=False),
        ),
    ]
