## Room-Booking App Django-Rest-Framework

**Yuklab Olish**
```
git clone https://github.com/fazliddinbaxtiyorov/Room-Booking-DRF.git
```
**Foydalanish**
```
 pip install -r requirements.txt
```
**Dasturni Ishlatish**
  * Dasturni pasdagi komandani terminal bilan ishga tushuring: 
```
python manage.py runserver
```


**Dasturni Boshqarish**

1. http://127.0.0.1:8000/api/rooms/ - Barcha xonalarni ko'rish uchun
2. http://127.0.0.1:8000/api/rooms/booked - Band qilgan xonalarni ko'rish uchun
3. http://127.0.0.1:8000/api/book/<int:room_number>/ - Xonalarni ko'rish uchun
4. http://127.0.0.1:8000/api/add/book/ - Xonani band qilish uchun
5. http://127.0.0.1:8000/api/update - Xonani update qilish uchun yoki vaqtini uzoqroq cho'zish uchun
6. http://127.0.0.1:8000/api/search/ - Date bo'yicha ma'lumot qidirish uchun
7. http://127.0.0.1:8000/api/migration - Migration
8. http://127.0.0.1:8000/signup/ - Ro'yhatdan o'tish uchun
9. http://127.0.0.1:8000/login/ - Kirish uchun
10. http://127.0.0.1:8000/api/docs - Dokumentatsiya
