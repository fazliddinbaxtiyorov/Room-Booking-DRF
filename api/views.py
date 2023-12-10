from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.filters import SearchFilter
from rest_framework import status
from .models import RoomModels, RoomBookingModels
from .serializers import RoomSerializers, RoomBookingSerializers, SomeSerializer


class RoomList(ListAPIView):
    queryset = RoomBookingModels.objects.all()
    serializer_class = RoomBookingSerializers
    permission_classes = [AllowAny]


class RoomIsBooked(ListAPIView):
    queryset = RoomModels
    serializer_class = SomeSerializer
    permission_classes = [AllowAny]

    def filter_queryset(self, queryset):
        queryset = super(RoomIsBooked, self).filter_queryset(queryset)
        return queryset.objects.filter(is_booked=True)


class RoomDetail(APIView):
    throttle_scope = 'detail'
    permission_classes = [AllowAny]

    def get(self, request, room_number):
        try:
            room = RoomModels.objects.get(id=room_number)
            return Response({"message": "Xona allaqachon boshqa bir mijoz tomonidan band qilingan!", "room": room.room,
                             'available_from': room.available_from}, status=status.HTTP_200_OK)
        except RoomModels.DoesNotExist:
            return Response({"message": "Xona topilmadi yoki mavjud emas xona raqami kiritildi!"},
                            status=status.HTTP_404_NOT_FOUND)


class RoomBook(CreateAPIView):
    queryset = RoomModels.objects.all()
    serializer_class = RoomSerializers
    throttle_scope = 'all'
    permission_classes = [IsAuthenticated]


class RoomSearch(ListAPIView):
    queryset = RoomBookingModels.objects.all()
    serializer_class = RoomBookingSerializers
    filter_backends = [SearchFilter]
    search_fields = ['date']
    permission_classes = [IsAuthenticated]


class RoomBookUpdate(UpdateAPIView):
    queryset = RoomModels.objects.all()
    serializer_class = RoomSerializers
    throttle_scope = 'all'
    lookup_field = 'id'
