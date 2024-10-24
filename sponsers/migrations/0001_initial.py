# Generated by Django 5.1.2 on 2024-10-24 01:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0002_delete_eventsponser'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EventSponser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('company_email', models.EmailField(max_length=254)),
                ('title', models.CharField(max_length=100)),
                ('offer', models.TextField()),
                ('sponserUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sponseringEvent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events_sponsers', to='events.event')),
            ],
        ),
    ]
