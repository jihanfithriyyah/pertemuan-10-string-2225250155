## Pertemuan 10 String dan Pengolahan Teks
Nama: Jihan Fithriyyah
NIM: [Isi NIM Anda]
Kelas: 3A (S1 Pendidikan Matematika)

## Tujuan
Tujuan dari praktikum dan tugas pada Pertemuan 10 ini adalah:
1. Memahami karakteristik tipe data string dalam Python sebagai urutan karakter yang bersifat immutable.
2. Mengaplikasikan operasi indexing, slicing, dan method bawaan string (strip, title, upper, lower, split, join, dll.) untuk memproses dan menormalisasi teks.
3. Menguji dan mendokumentasikan program pengolahan teks berbasis data pembelajaran menggunakan Visual Studio Code dan GitHub.

## Cara Menjalankan
1. Menjalankan File LatihanUntuk menjalankan latihan 1 hingga 6, jalankan perintah berikut pada terminal di dalam folder utama repositori:
python3 latihan/01_dasar_string.py
python3 latihan/02_indeks_slicing.py
python3 latihan/03_method_string.py
python3 latihan/04_bersihkan_teks.py
python3 latihan/05_split_join.py
python3 latihan/06_pencarian_kata.py
2. Menjalankan Program Tugas 4
Untuk menjalankan program utama Tugas 4 (Normalisasi Data Mahasiswa), jalankan perintah berikut:
python3 tugas/normalisasi_data_mahasiswa.py

## Algoritma
Proses pembersihan dan normalisasi data teks pada program Tugas 4 dilakukan melalui alur langkah berikut:
1. Normalisasi Nama Lengkap (normalisasi_nama):
- Menghapus spasi berlebih pada bagian awal dan akhir string menggunakan .strip().
- Memecah string nama menjadi list kata dengan .split() untuk secara otomatis menghilangkan spasi ganda atau tak beraturan di antara kata.
- Menggabungkan kembali kumpulan kata tersebut menggunakan  " ".join()
- Mengubah bentuk huruf awal setiap kata menjadi kapital (title case) menggunakan .title().
2. Membuat Inisial Mahasiswa (buat_inisial):
- Memanggil nama yang telah dinormalisasi.
- Memecah nama bersih menjadi daftar kata menggunakan .split().
- Mengambil karakter pertama pada indeks [0] dari setiap kata dalam daftar.
- Menggabungkan seluruh karakter awal tersebut menjadi string tunggal menggunakan "".join().
3. Normalisasi Kode Kelas (normalisasi_kode):
- Menghapus spasi di awal dan akhir dengan .strip().
- Mengubah seluruh huruf menjadi huruf kapital (upper case) menggunakan .upper().
- Memecah string berdasarkan whitespace dengan .split().
- Menggabungkan kembali potongan-potongan kode tersebut dengan separator tanda hubung menggunakan "-".join().
4. Output:
- Menghitung total jumlah kata nama lengkap dengan fungsi len() pada hasil split().
- Menampilkan hasil normalisasi nama, kode kelas, jumlah kata, dan inisial secara rapi ke layar.

## Test Case
Tabel pengujian berikut mencakup test case wajib dari modul serta pengujian data mandiri:

| No | Input Nama & Kode | Hasil Harapan | Hasil Aktual | Status |
|---|---|---|---|---|
| 1 | **Nama:** `ahmad muhammad`<br>**Kode:** `pmat a 2026` | Nama: `Ahmad Muhammad`<br>Kode: `PMAT-A-2026`<br>Inisial: `AM`<br>Jml Kata: `2` | Nama: `Ahmad Muhammad`<br>Kode: `PMAT-A-2026`<br>Inisial: `AM`<br>Jml Kata: `2` | Lulus |
| 2 | **Nama:** `fATHIYYAH MUTHMAINNAH`<br>**Kode:** `kelas b` | Nama: `Fathiyyah Muthmainnah`<br>Kode: `KELAS-B`<br>Inisial: `FM`<br>Jml Kata: `2` | Nama: `Fathiyyah Muthmainnah`<br>Kode: `KELAS-B`<br>Inisial: `FM`<br>Jml Kata: `2` | Lulus |
| 3 | **Nama:** `BUDI`<br>**Kode:** `pmtk 01` | Nama: `Budi`<br>Kode: `PMTK-01`<br>Inisial: `B`<br>Jml Kata: `1` | Nama: `Budi`<br>Kode: `PMTK-01`<br>Inisial: `B`<br>Jml Kata: `1` | Lulus |
| 4 | **Nama:** `siti nur aisyah`<br>**Kode:** `kelas c` | Nama: `Siti Nur Aisyah`<br>Kode: `KELAS-C`<br>Inisial: `SNA`<br>Jml Kata: `3` | Nama: `Siti Nur Aisyah`<br>Kode: `KELAS-C`<br>Inisial: `SNA`<br>Jml Kata: `3` | Lulus |
| 5 | **Nama:** `jihan fithriyyah`<br>**Kode:** `pmat a 3a` | Nama: `Jihan Fithriyyah`<br>Kode: `PMAT-A-3A`<br>Inisial: `JF`<br>Jml Kata: `2` | Nama: `Jihan Fithriyyah`<br>Kode: `PMAT-A-3A`<br>Inisial: `JF`<br>Jml Kata: `2` | Lulus |

## Refleksi
- Masalah Pengolahan Teks yang Ditemukan:
Masalah utama yang ditemukan adalah input nama dan kode kelas yang sering kali memiliki spasi berlebih tidak teratur di tengah teks (misalnya spasi ganda atau tiga spasi berturut-turut), serta variasi kapitalisasi yang tidak konsisten (campuran huruf besar dan kecil). Penggunaan .strip() saja tidak cukup untuk menghapus spasi tak beraturan di tengah teks.
- Cara Memperbaiki / Solusi:
Solusi yang diterapkan adalah mengombinasikan .split() tanpa parameter dan .join(). Metode .split() secara otomatis memisahkan string berdasarkan spasi berlebih berapa pun jumlahnya dan mengabaikannya. Setelah menjadi list kata bersih, kita dapat menggabungkannya kembali dengan " ".join() untuk nama atau "-".join() untuk kode kelas. Kombinasi ini dikemas ke dalam fungsi terpisah agar kodenya modular, mudah dibaca, dan dapat digunakan kembali (reusable).