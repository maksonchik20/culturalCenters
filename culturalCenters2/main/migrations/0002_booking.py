# Generated by Django 4.2.7 on 2023-11-30 16:57

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("main", "0001_initial")
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateField(verbose_name='Дата создания')),
                ('date_start', models.DateTimeField(verbose_name='Дата начала бронирования')),
                ('date_end', models.DateTimeField(verbose_name='Дата окончания бронирования')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('cnt_section', models.PositiveIntegerField(default=1, verbose_name='Количество забронированных частей')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.event', verbose_name='Мероприятие')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.room', verbose_name='Помещение')),
            ],
            options={
                'verbose_name': 'Бронирование',
                'verbose_name_plural': 'Бронирования',
            },
        ),
    ]
