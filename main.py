from model import daftar_nilai
from view import view_nilai

data = {'nama' : [], 'nilai' : []}
while True:
    print("[ (l)ihat , (t)ambah, (c)ari (u)bah, (h)apus, (k)eluar ] \n")
    tanya = input("Masukkan Pilihan : ")
    match tanya:
        case "l":
            view_nilai.cetak_daftar_nilai(data)
        case "t":
            data = daftar_nilai.tambah_data(data)
        case "u":
            view_nilai.cetak_daftar_nilai(data)
            if len(data['nama']) > 0:
                nama = input("masukkan nama siswa yang akan diubah : ")
                data = daftar_nilai.ubah_data(data, nama)
        case "c":
            # view_nilai.cetak_daftar_nilai(data)
            if len(data['nama']) > 0:
                nama = input("masukkan nama siswa yang akan dicari : ")
                daftar_nilai.cari_data(data, nama)
        case "h":
            view_nilai.cetak_daftar_nilai(data)
            if len(data['nama']) > 0:
                nama = input("masukkan nama siswa yang akan dihapus : ")
                data = daftar_nilai.hapus_data(data, nama)
        case "k":
            print("anda sudah Keluar dari program")
            break
        case _:
            print("Tidak Sesuai Pilihan, Silahkan Pilih Kembali!!\n")
            continue
