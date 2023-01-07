from model.daftar_nilai import x


def header():
    print("===========================")
    print("|   Program Input Nilai   |")
    print("===========================")


def kode_salah():
    CRED = '\033[91m'
    CEND = '\033[0m'
    print(CRED + "KODE YANG ANDA MASUKKAN SALAH!\nSILAHKAN INPUT ULANG KODE YANG BENAR." + CEND)


def tampilkan():
    if x.items():
        print("---------------------------------------------------------------------------------")
        print("\n                               DAFTAR NILAI MAHASISWA                    ")
        print("---------------------------------------------------------------------------------")
        print("| No |      Nama      |     NIM     |  Tugas  |   UTS   |   UAS   |    Akhir    |")
        print("---------------------------------------------------------------------------------")
        i = 0
        for b in x.items():
            i += 1
            print("| {no:2d} | {0:14s} | {1:11s} | {2:7d} | {3:7d} | {4:7d} | {5:7f}   |"
                  .format(b[0][: 14], b[1][0], b[1][1], b[1][2], b[1][3], b[1][4], no=i))
        print("---------------------------------------------------------------------------------")
    else:
        print("---------------------------------------------------------------------------------")
        print("\n                               DAFTAR NILAI MAHASISWA                    ")
        print("---------------------------------------------------------------------------------")
        print("| No |      Nama      |     NIM     |  Tugas  |   UTS   |   UAS   |    Akhir    |")
        print("---------------------------------------------------------------------------------")
        print("|                                TIDAK ADA DATA                                 |")
        print("---------------------------------------------------------------------------------")


def cari():
    from view.input_nilai import cari
    cari()