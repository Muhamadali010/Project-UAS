def input_data():
    from modul.daftar_nilai import tambah
    nama = input("Masukkan Nama Mahasiswa   : ")
    nim = input("Masukkan NIM              : ")
    tugas = int(input("Masukkan Nilai Tugas      : "))
    uts = int(input("Masukkan Nilai UTS        : "))
    uas = int(input("Masukkan Nilai UAS        : "))
    tambah(nama, nim, tugas, uts, uas)
def ubah_data():
    from modul.daftar_nilai import ubah
    ubah(nama=input("Masukkan Nama Mahasiswa   : "))
def hapus_data():
    from modul.daftar_nilai import hapus
    hapus(nama=input("Masukkan Nama Mahasiswa   : "))
def cari():
    from modul.daftar_nilai import cari
    cari(nama=input("Masukkan Nama Mahasiswa   : "))