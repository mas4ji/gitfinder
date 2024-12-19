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

2. **Masuk ke direktori proyek**

   Setelah berhasil meng-clone repositori, masuk ke direktori GitLeakHunter:

   ```bash
   cd GitLeakHunter

4. **Install dependensi**

   Instal semua dependensi yang diperlukan dengan pip. Jalankan perintah berikut:

   ```bash
   pip install -r requirements.txt

## 🛠 Instalasi GitLeakHunter

Setelah Anda berhasil menginstal **GitLeakHunter**, Anda dapat mulai menggunakannya untuk memindai domain atau subdomain untuk file `.git` yang terekspos. Berikut adalah cara menggunakan alat ini.

### 1. **Memindai Domain Tunggal**

   Untuk memindai satu domain atau subdomain, jalankan perintah berikut:

   ```bash
   python3 gitt.py -d example.com
