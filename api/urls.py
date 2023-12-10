from django.urls import path
from .views import RoomList, RoomDetail, RoomBook, RoomSearch, RoomIsBooked, RoomBookUpdate

urlpatterns = [
    path('api/rooms/', RoomList.as_view()),
    path('api/rooms/booked', RoomIsBooked.as_view()),
    path('api/book/<int:room_number>/', RoomDetail.as_view()),
    path('api/add/book/', RoomBook.as_view()),
    path('api/update', RoomBookUpdate.as_view()),
    path('api/search/', RoomSearch.as_view())
]
