# Generated by Django 5.1.1 on 2024-10-26 07:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approvalStatus', models.BooleanField()),
                ('date', models.DateField()),
                ('groomer', models.CharField(max_length=100)),
                ('trailName', models.CharField(choices=[('Shrine Pass', 'Shrine Pass'), ('Owl Creek Road', 'Owl Creek Road')], max_length=100)),
                ('report', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Trails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trailname', models.CharField(max_length=100)),
                ('location', models.CharField(choices=[('Front Range', 'Front Range'), ('San Juans', 'San Juans')], max_length=100)),
                ('rating', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
            ],
        ),
    ]
