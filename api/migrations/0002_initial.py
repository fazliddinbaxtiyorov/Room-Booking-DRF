# Generated by Django 4.2 on 2023-12-10 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomBookingModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rooms', models.TextField(max_length=2000)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='RoomModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(default='Xona Band Qilindi!', editable=False, max_length=2222)),
                ('room', models.CharField(blank=True, choices=[('Facebook', 'Facebook'), ('Google', 'Google'), ('Amazon', 'Amazon'), ('Netflix ', 'Netflix '), ('Hulu', 'Hulu'), ('McDonalds', 'McDonalds'), ('Halloween', 'Halloween'), ('New York', 'New York')], max_length=2222)),
                ('start', models.TimeField(blank=True, max_length=2222)),
                ('end', models.TimeField(blank=True, max_length=2222)),
                ('available_from', models.CharField(blank=True, max_length=2222)),
                ('is_booked', models.BooleanField(blank=True, default=False)),
            ],
        ),
    ]
