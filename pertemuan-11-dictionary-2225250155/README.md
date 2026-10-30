# Pertemuan 11 Dictionary/Map

* **Nama:** Jihan Fithriyyah
* **NIM:** 2225250155
* **Kelas:** 3A
* **Program Studi:** S1 Pendidikan Matematika

## Tujuan
Memodelkan data pendidikan menggunakan *dictionary* dan pasangan *key-value* dalam bahasa pemrograman Python.

## Struktur Data
Data mahasiswa dimodelkan menggunakan *nested dictionary* (dictionary bersarang).
* **Key Utama:** Nomor Induk Mahasiswa / NIM (misal: `"2225250155"`, `"A002"`, dst.) sebagai pengenal unik.
* **Value:** Berupa *dictionary* yang menyimpan atribut informasi mahasiswa, yaitu:
  * `nama` (String): Nama lengkap mahasiswa
  * `kelas` (String): Kelas mahasiswa (misal: `"3A"`, `"3B"`)
  * `nilai` (Integer): Nilai hasil belajar mahasiswa

## Cara Menjalankan
1. Jalankan program utama `data_mahasiswa.py` melalui terminal VS Code dengan perintah:
   ```bash
   python3 praktik/data_mahasiswa.py
   
   Untuk menjalankan file latihan individual (misal Latihan 01):
   python3 latihan/01_dasar_dictionary.py

## Test Case
| Kasus | Input / Aksi | Hasil yang Diharapkan | Hasil Aktual | Status |
| :--- | :--- | :--- | :--- | :--- |
| Pencarian tersedia | 2225250155 | Data Jihan Fithriyyah ditampilkan | Data Jihan Fithriyyah tampil | Berhasil |
| Pencarian tidak tersedia | A999 | Pesan 'Data tidak ditemukan' | Pesan 'Data tidak ditemukan' tampil | Berhasil |
| Pembaruan nilai | NIM A002 menjadi 82 | Nilai A002 berubah menjadi 82 | Nilai A002 berhasil berubah jadi 82 | Berhasil |
| Penambahan data | NIM A006 | Key A006 tersedia setelah ditambahkan | Key A006 beserta data baru tampil | Berhasil |
| Rekap | items() | Semua NIM dan detail data mahasiswa tampil | Seluruh pasangan key-value tampil | Berhasil |

## Refleksi
Selama pengerjaan, kesalahan akses key yang perlu dihindari adalah memanggil key yang belum terdaftar menggunakan kurung siku secara langsung (misalnya data["kelas"]), karena hal tersebut memicu kegagalan program berupa KeyError. Kesalahan ini berhasil diatasi dengan menggunakan fungsi akses aman .get() yang mengembalikan nilai None atau nilai default ketika key tidak ditemukan, serta menggunakan pengecekan keberadaan key dengan operator in.