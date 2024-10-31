# Generated by Django 5.1.1 on 2024-10-31 04:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corduroyserver', '0007_alter_trails_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reports',
            name='trailName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corduroyserver.trails'),
        ),
        migrations.AlterField(
            model_name='trails',
            name='trailName',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]