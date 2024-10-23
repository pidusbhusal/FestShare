# Generated by Django 3.2.25 on 2024-10-23 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money_tracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploader', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='event_images/')),
                ('participants', models.IntegerField(default=0)),
                ('max_participants', models.IntegerField(default=30)),
            ],
        ),
    ]
