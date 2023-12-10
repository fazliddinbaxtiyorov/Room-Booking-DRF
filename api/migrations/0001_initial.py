# Generated by Django 4.2 on 2023-12-10 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]
    def create_room_booking_models(apps, schema_manager):
        """
        Creates the room booking models table.
        """
        apps.create_model('api_roombookingmodels', 'RoomBooking', (
            'id', models.AutoField(primary_key=True),
            'room', models.ForeignKey('rooms.Room', on_delete=models.CASCADE),
            'date', models.DateField(),
        ))
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

