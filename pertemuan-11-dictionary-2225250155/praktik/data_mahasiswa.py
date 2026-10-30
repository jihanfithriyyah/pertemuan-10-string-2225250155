def cari_mahasiswa(data, nim):
    return data.get(nim)

def rata_rata_nilai(data):
    if len(data) == 0:
        return 0
    total = 0
    for info in data.values():
        total += info["nilai"]
    return total / len(data)

# Memodelkan data mahasiswa dengan NIM utama milik Jihan Fithriyyah[cite: 10, 11]
data_mahasiswa = {
    "2225250155": {"nama": "Jihan Fithriyyah", "kelas": "3A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "3A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "3B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "3B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "3A", "nilai": 88}
}

# Pengujian pencarian data yang tersedia
nim = "2225250155"
hasil = cari_mahasiswa(data_mahasiswa, nim)
print(f"Pencarian {nim}:")
if hasil is not None:
    print(hasil)
else:
    print("Data tidak ditemukan")

print("-" * 30)

# Penambahan mahasiswa baru
data_mahasiswa["A006"] = {
    "nama": "Fajar",
    "kelas": "3B",
    "nilai": 80
}

# Pembaruan nilai mahasiswa A002 menjadi 82[cite: 11]
data_mahasiswa["A002"]["nilai"] = 82

# Menampilkan seluruh data menggunakan items()[cite: 11]
print("Rekap Seluruh Data Mahasiswa:")
for nim, info in data_mahasiswa.items():
    print(f"{nim}: {info}")

print("-" * 30)
# Menghitung rata-rata nilai seluruh mahasiswa[cite: 11]
print(f"Rata-rata Nilai Kelas = {rata_rata_nilai(data_mahasiswa):.2f}")