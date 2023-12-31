# Generated by Django 4.2.3 on 2023-07-29 05:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField(verbose_name='Slot Date')),
                ('start_time', models.TimeField(verbose_name='Slot Start Time')),
                ('end_time', models.TimeField(verbose_name='Slot End Time')),
                ('is_booked', models.BooleanField(default=False, verbose_name='Is Booked')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_slots', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Slot',
            },
        ),
        migrations.AddConstraint(
            model_name='slot',
            constraint=models.CheckConstraint(check=models.Q(('end_time__gt', models.F('start_time'))), name='check_slot-time'),
        ),
        migrations.AddConstraint(
            model_name='slot',
            constraint=models.UniqueConstraint(fields=('date', 'start_time', 'end_time'), name='unique_booking_date_time'),
        ),
    ]
