from django.db import models


# Create your models here.

class RoomBookingModels(models.Model):
    rooms = models.TextField(max_length=2000)
    date = models.DateField()


class RoomModels(models.Model):
    ROOM_CHOICES = (
        ('Facebook', 'Facebook'),
        ('Google', 'Google'),
        ('Amazon', 'Amazon'),
        ('Netflix ', 'Netflix '),
        ('Hulu', 'Hulu'),
        ('McDonalds', 'McDonalds'),
        ('Halloween', 'Halloween'),
        ('New York', 'New York'),
    )
    message = models.CharField(max_length=2222, default='Xona Band Qilindi!', editable=False)
    room = models.CharField(max_length=2222, choices=ROOM_CHOICES, blank=True)
    start = models.TimeField(max_length=2222, blank=True)
    end = models.TimeField(max_length=2222, blank=True)
    available_from = models.CharField(max_length=2222, blank=True)
    is_booked = models.BooleanField(default=False, blank=True)
