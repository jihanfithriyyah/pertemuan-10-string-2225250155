def normalisasi_nama(nama):
    # Menghapus spasi berlebih di awal/akhir, merapikan spasi di tengah, lalu format title case
    return " ".join(nama.strip().split()).title()

def buat_inisial(nama):
    # Mengambil huruf awal dari setiap kata pada nama bersih
    nama_bersih = normalisasi_nama(nama)
    kata = nama_bersih.split()
    return "".join(k[0] for k in kata)

def normalisasi_kode(kode):
    # Membersihkan spasi, mengubah ke huruf kapital, memecah, lalu menggabungkan dengan tanda hubung (-)
    kata = kode.strip().upper().split()
    return "-".join(kata)

if __name__ == "__main__":
    # Menerima input dari pengguna
    nama = input("Masukkan nama: Jihan Fithriyyah")
    kode = input("Masukkan kode kelas: 3A")

    # Memproses data menggunakan fungsi
    nama_bersih = normalisasi_nama(nama)
    kode_bersih = normalisasi_kode(kode)
    inisial = buat_inisial(nama)
    jumlah_kata = len(nama_bersih.split())

    # Menampilkan hasil normalisasi secara rapi
    print(f"Nama bersih : {nama_bersih}")
    print(f"Kode kelas  : {kode_bersih}")
    print(f"Jumlah kata : {jumlah_kata}")
    print(f"Inisial     : {inisial}")