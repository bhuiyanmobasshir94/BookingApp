# Generated by Django 4.2.3 on 2023-07-29 05:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('code', models.CharField(max_length=5, verbose_name='Code')),
            ],
            options={
                'verbose_name': 'Country',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('address', models.TextField(verbose_name='Address')),
                ('phone', models.CharField(max_length=100, verbose_name='Phone')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slot_countries', to='booking.country')),
                ('slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slot_bookings', to='booking.slot')),
            ],
            options={
                'verbose_name': 'Booking',
            },
        ),
    ]