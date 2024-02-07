# TTG-Andre Setiawan

Soal Nomor 1 : 
Jalankan file home.html pada browser

Soal Nomor 2 : 
Pastikan python telah terinstall
Pada console, eksekusi file stopwatch.py dengan "python stopwatch.py". Setelah itu, akan muncul tampilan GUI aplikasi stopwatch.

Soal Nomor 3 : 
Frontend (Vue JS) : 
1. Install Vue JS : npm install -g @vue/cli
2. Dari directory ttgapi-frontend, install requirements sebagai berikut : 
- npm install bootstrap@4.6.0 jquery popper.js
- npm install vue-router@4
- npm install axios
3. Jalankan dengan npm run serve. Frontend akan berjalan pada localhost:8081

Backend (Django + MySql) : 
1. Jalankan virtual environment pada folder ttgapi, dengan mengetik perintah env\Scripts\activate
2. (MySql) Buat database baru bernama ttgapi. Port pada settings.py di set ke 3306. Jika menggunakan port lain, bisa disesuaikan dengan port yang digunakan saat ini
3. Install requirements sebagai berikut :
- pip install django
- pip install djangorestframework
- pip install django-cors-headers
- pip install pymysql
4. Jalankan python manage.py migrate untuk migrasi models ke database
5. Jalankan Django dengan masuk ke folder ttgapi, lalu ketik perintah python manage.py runserver. Backend akan berjalan pada localhost:8000

Soal Nomor 4 : 
Pastikan python telah terinstall
Terdapat 2 fungsi pada main.py, yaitu piramida() dan kelompok_bilangan_genap(). Pada console, eksekusi kedua fungsi tersebut dengan "python main.py", untuk memperoleh output program dalam bentuk console
