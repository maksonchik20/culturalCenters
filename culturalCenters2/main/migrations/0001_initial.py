# Generated by Django 4.2.7 on 2023-11-30 16:57

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Вид мероприятия')),
            ],
            options={
                'verbose_name': 'Вид мероприятия',
                'verbose_name_plural': 'Виды мероприятий',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Дата мероприятия')),
                ('time', models.TimeField(verbose_name='Время мероприятия')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='type_event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.eventtype',
                                    verbose_name='Вид мероприятия'),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название помещения')),
                ('cnts', models.PositiveIntegerField(default=1, help_text='Если этот параметр равен 0, то помещение нельзя забронировать.\n    Если же равен 1, то помещение можно забронировать только целиком.\n    Если же равен x, то помещение можно разделить(забронировать) на x частей.', verbose_name='Количество частей помещения')),
            ],
            options={
                'verbose_name': 'Помещение',
                'verbose_name_plural': 'Помещения',
            },
        ),
        migrations.CreateModel(
            name='WorkType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название вида работы')),
            ],
            options={
                'verbose_name': 'Вид работы',
                'verbose_name_plural': 'Виды работ',
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата регистрации заявки')),
                ('time', models.TimeField(verbose_name='Время регистрации заявки')),
                ('date_end', models.DateField(default=datetime.date.today, verbose_name='Конечная дата выполнения заявки')),
                ('time_end', models.TimeField(default=django.utils.timezone.now, verbose_name='Конечное время выполнения заявки')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('status', models.CharField(choices=[('Создана(черновик)', 'Создана(черновик)'), ('К выполнению', 'К выполнению'), ('Выполнена', 'Выполнена')], default='Создана(черновик)', max_length=255, verbose_name='Статус заявки')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.event', verbose_name='Мероприятие')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.room', verbose_name='Помещение')),
                ('work_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.worktype', verbose_name='Вид работы')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]