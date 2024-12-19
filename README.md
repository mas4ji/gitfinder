# GitLeakHunter ![GitLeakHunter](https://img.shields.io/badge/Tool-GitLeakHunter-brightgreen)

**GitLeakHunter** adalah alat untuk mendeteksi dan memindai file `.git` yang terekspos di domain atau subdomain. Alat ini digunakan untuk mencari file dan direktori `.git` yang seharusnya tidak dapat diakses publik, yang bisa berisiko bagi keamanan dan privasi.

Dengan **GitLeakHunter**, Anda dapat dengan cepat memeriksa apakah suatu website atau aplikasi web memiliki konfigurasi Git yang terbuka, yang berpotensi membocorkan informasi sensitif.

## 🚀 Fitur

- 🔍 Memindai domain atau subdomain untuk mendeteksi file `.git`.
- 🔐 Mengidentifikasi file atau direktori Git yang terekspos seperti `.git/config`, `.git/HEAD`, dan `.git/objects/`.
- 📊 Memberikan hasil yang mudah dibaca dengan status "Vulnerable" atau "Not Vulnerable".
- 📝 Dapat digunakan untuk memindai satu domain atau daftar domain dari file teks.

## 🛠 Instalasi

### Prasyarat

Pastikan Anda memiliki **Python 3.x** yang terinstal di sistem Anda. Anda juga perlu menginstal beberapa dependensi yang diperlukan.
