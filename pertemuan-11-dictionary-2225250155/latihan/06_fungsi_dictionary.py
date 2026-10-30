def cari(data, nim):
    return data.get(nim, "Data tidak ditemukan")

mahasiswa = {
    "2225250155": {"nama": "Jihan Fithriyyah", "nilai": 85},
    "A002": {"nama": "Budi", "nilai": 78}
}
print(cari(mahasiswa, "2225250155"))
print(cari(mahasiswa, "A003"))