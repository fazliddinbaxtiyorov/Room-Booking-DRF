from rest_framework import serializers
from .models import RoomBookingModels, RoomModels


class RoomBookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = RoomBookingModels
        fields = ['rooms', 'date']


class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = RoomModels
        fields = '__all__'


class SomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomModels
        fields = ['room']