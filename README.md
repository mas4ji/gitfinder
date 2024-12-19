# GitLeakHunter ![GitLeakHunter](https://img.shields.io/badge/Tool-GitLeakHunter-brightgreen)

**GitLeakHunter** adalah alat untuk mendeteksi dan memindai file `.git` yang terekspos di domain atau subdomain. Alat ini digunakan untuk mencari file dan direktori `.git` yang seharusnya tidak dapat diakses publik, yang bisa berisiko bagi keamanan dan privasi.

Dengan **GitLeakHunter**, Anda dapat dengan cepat memeriksa apakah suatu website atau aplikasi web memiliki konfigurasi Git yang terbuka, yang berpotensi membocorkan informasi sensitif.

## 🚀 Fitur

- 🔍 Memindai domain atau subdomain untuk mendeteksi file `.git`.
- 🔐 Mengidentifikasi file atau direktori Git yang terekspos seperti `.git/config`, `.git/HEAD`, dan `.git/objects/`.
- 📊 Memberikan hasil yang mudah dibaca dengan status "Vulnerable" atau "Not Vulnerable".
- 📝 Dapat digunakan untuk memindai satu domain atau daftar domain dari file teks.

## 🛠 Instalasi GitLeakHunter

Berikut adalah langkah-langkah untuk menginstal dan menjalankan **GitLeakHunter** di sistem Anda.

### Persyaratan

Sebelum mulai menginstal, pastikan Anda memiliki beberapa perangkat lunak yang diperlukan di sistem Anda:

- **Python 3.x** atau lebih tinggi
- **pip** untuk mengelola paket Python

### Langkah-langkah Instalasi

Ikuti langkah-langkah berikut untuk menginstal **GitLeakHunter** di sistem Anda.

1. **Clone repository ini**

   Pertama, clone repositori GitHub ke sistem Anda menggunakan perintah berikut di terminal:

   ```bash
   git clone https://github.com/mas4ji/GitLeakHunter.git
