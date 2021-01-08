import os
import csv
import time
import datetime


fileUser = 'data_user.csv'
fileBelanja = 'data_belanja.csv'

dataUser = []
dataBelanja = []

total = 0
tanggal = datetime.datetime.today().strftime('%Y-%m-%d')


def hapusLayar():
    os.system('cls' if os.name == 'nt' else 'clear')


def backToLauncher():
    print("\n")
    input("Tekan Enter Untuk Kembali.....")
    launcher()


def backToLogin():
    print("\n")
    input("Tekan Enter Untuk Login Kembali....")
    login()


def backToPesanan():
    print("\n")
    input("Tekan Enter Untuk Lanjut....")
    buatPesanan()


def launcher():
    hapusLayar()
    print("{0:^50}".format("Selamat Datang"))
    print("{0:^50}".format("Silahkan login/register terlebih dahulu"))
    print("-" * 50)
    print("[1] Login")
    print("[2] Register")
    print("[0] Exit")
    print("-" * 50)
    print("\n")
    pilihMenu = input("Pilih Menu=> ")
    if pilihMenu == "1":
        login()
    elif pilihMenu == "2":
        register()
    elif pilihMenu == "0":
        exit(0)
    else:
        print("Menu yang anda masukkan salah!!")
        backToLauncher()


def login():
    hapusLayar()
    user = []
    print("{0:^50}".format("Login Page"))
    print("-"*50)
    username = input("Masukkan username anda: ")
    password = input("Masukkan password anda: ")
    try:
        with open(fileUser, 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for data in reader:
                user.append(data)

            for data in user:
                if username == data['username'] and password == data['password']:
                    dataUser.append(data)
                    mainMenu()
                else:
                    continue

            if len(dataUser) == 0:
                print("Username/Password Yang Anda Masukkan Salah!!!")

    except IOError:
        print("Belum Ada Akun Yang Terdaftar, Silahkan Register Terlebih Dahulu!!")
    backToLauncher()


def register():
    hapusLayar()

    try:
        with open(fileUser, 'r') as csvfile:
            csv.DictReader(csvfile, delimiter=',')

    except IOError:
        header = ['nama', 'username',
                  'password', 'tglLahir', 'alamat', 'tglDaftar']
        with open(fileUser, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=header)
            writer.writeheader()
    tambahUser()


def tambahUser():
    print("{0:^50}".format("Register Page"))
    print("-"*50)
    nama = input("Masukkan Nama Lengkap Anda: ")
    username = input("Masukkan Username Anda: ")
    password = input("Masukkan Password Anda: ")
    tglLahir = input("Masukkan Tanggal Lahir Anda: ")
    alamat = input("Masukkan Alamat Anda: ")
    tglDaftar = datetime.datetime.today().strftime('%Y-%m-%d')

    dictUser = dict()

    dictUser['nama'] = nama
    dictUser['username'] = username
    dictUser['password'] = password
    dictUser['tglLahir'] = tglLahir
    dictUser['alamat'] = alamat
    dictUser['tglDaftar'] = tglDaftar

    header = ['nama', 'username',
              'password', 'tglLahir', 'alamat', 'tglDaftar']

    try:
        with open(fileUser, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=header)
            writer.writerow(dictUser)

        print("Akun Berhasil Didaftarkan")
        backToLauncher()
    except IOError:
        print("Tidak Ada Data")
    backToLauncher()


def mainMenu():
    hapusLayar()
    print("{0:^50}".format("Welcome To RESTECHNO"))
    print("{0:^50}".format("Silahkan Memilih Menu Yang Ditampilkan"))
    print("-" * 50)
    for data in dataUser:
        print(f"Nama User: {data['nama']}", " "*13, f"Tanggal: {tanggal}")
    print("-" * 50)
    print("[1] Buat Pesanan Baru")
    print("[2] Riwayat Transaksi")
    print("[3] Profile")
    print("[4] Hapus Akun Ini")
    print("[5] Logout")
    print("[0] Exit")
    print("-" * 50)
    menu = input("Pilih Menu=> ")

    if menu == "1":
        buatPesanan()
    elif menu == "2":
        riwayatTransaksi()
    elif menu == "3":
        profile()
    elif menu == "4":
        hapusAkun()
    elif menu == "5":
        dataUser.clear()
        backToLauncher()
    elif menu == "0":
        exit(0)
    else:
        print("Menu Yang Anda Masukkan Salah")
        print("\n")
        input("Tekan Enter Untuk Memasukkan Kembali...")
        mainMenu()


def buatPesanan():
    hapusLayar()
    print("{0:^50}".format("Welcome To RESTECHNO"))
    print("{0:^50}".format("Silahkan Memilih Menu Yang Ditampilkan"))
    print("-" * 50)
    for data in dataUser:
        print(f"Nama User: {data['nama']}", " "*13, f"Tanggal: {tanggal}")
    print("-" * 50)
    print("[1] Pesan Makanan")
    print("[2] Pesan Minuman")
    print("[3] Keranjang")
    print("[4] Batalkan Pesanan")
    print("[5] Checkout")
    print("[6] Kembali")
    print("[0] Exit")
    print("-" * 50)
    pilihMenu = input("Pilih Menu=> ")

    if pilihMenu == "1":
        makanan()
    elif pilihMenu == "2":
        minuman()
    elif pilihMenu == "3":
        keranjang()
    elif pilihMenu == "4":
        batalkanPesanan()
    elif pilihMenu == "5":
        checkout()
    elif pilihMenu == "6":
        mainMenu()
    elif pilihMenu == "0":
        exit(0)
    else:
        print("Menu Yang Anda Masukkan Salah")
        backToPesanan()


def riwayatTransaksi():
    hapusLayar()
    print("{0:^50}".format("Welcome To RESTECHNO"))
    print("{0:^50}".format("Silahkan Memilih Menu Yang Ditampilkan"))
    print("-" * 50)
    for data in dataUser:
        print(f"Nama User: {data['nama']}", " "*13, f"Tanggal: {tanggal}")
    print("-" * 50)
    print("[1] Lihat Riwayat Transaksi")
    print("[2] Hapus Riwayat Transaksi")
    print("[3] Kembali")
    print("[0] Exit")
    print("-" * 50)
    pilihMenu = input("Pilih Menu=> ")

    if pilihMenu == "1":
        lihatRiwayatPesanan()
    elif pilihMenu == "2":
        hapusRiwayatPesanan()
        input("Tekan Enter Untuk Lanjut...")
        mainMenu()
    elif pilihMenu == "3":
        buatPesanan()
    elif pilihMenu == "0":
        exit(0)
    else:
        print("Menu Yang Anda Masukkan Salah")
        backToPesanan()


def makanan():
    command = 'y'
    global namaUser
    global total
    while True:
        if command == 'y':
            hapusLayar()
            print("{0:^50}".format("Welcome To RESTECHNO"))
            print("{0:^50}".format("Silahkan Memilih Makanan Yang Akan Dipesan"))
            print("-" * 50)
            for data in dataUser:
                print(f"Nama User: {data['nama']}",
                      " "*13, f"Tanggal: {tanggal}")
                namaUser = data['nama']
            print("-" * 50)

            print("[1] Nasi Goreng - Rp. 11.000")
            print("[2] Nasi Mawut - Rp 13.000")
            print("[3] Mie Goreng - Rp.10.000")
            print("[4] Mie Kuah - Rp.10.000")
            print("[5] Kembali")
            print("[0] Exit")
            print("-"*50)
            pilihMakanan = input("Pilih Makanan=> ")
            porsi = int(input("Porsi Yang Dipesan: "))

            if pilihMakanan == "1":
                namaMakanan = "Nasi Goreng"
                jenisMenu = "Makanan"
                porsiDipesan = porsi
                hargaMakanan = 11000
                totalSementara = hargaMakanan*porsi
                total += totalSementara
                dataMakanan = {'Tanggal Pesan': tanggal, 'Nama Pemesan': namaUser, 'Nama Menu': namaMakanan, 'Jenis Menu': jenisMenu, 'Porsi Dipesan': porsiDipesan,
                               'Harga': hargaMakanan, 'Total Sementara': totalSementara, 'Total Keseluruhan': total}
                dataBelanja.append(dataMakanan)
            elif pilihMakanan == "2":
                namaMakanan = "Nasi Mawut"
                jenisMenu = "Makanan"
                porsiDipesan = porsi
                hargaMakanan = 13000
                totalSementara = hargaMakanan*porsi
                total += totalSementara
                dataMakanan = {'Tanggal Pesan': tanggal, 'Nama Pemesan': namaUser, 'Nama Menu': namaMakanan, 'Jenis Menu': jenisMenu,
                               'Porsi Dipesan': porsiDipesan, 'Harga': hargaMakanan, 'Total Sementara': totalSementara, 'Total Keseluruhan': total}
                dataBelanja.append(dataMakanan)
            elif pilihMakanan == "3":
                namaMakanan = "Mie Goreng"
                jenisMenu = "Makanan"
                porsiDipesan = porsi
                hargaMakanan = 10000
                totalSementara = hargaMakanan*porsi
                total += totalSementara
                dataMakanan = {'Tanggal Pesan': tanggal, 'Nama Pemesan': namaUser, 'Nama Menu': namaMakanan, 'Jenis Menu': jenisMenu,
                               'Porsi Dipesan': porsiDipesan, 'Harga': hargaMakanan, 'Total Sementara': totalSementara, 'Total Keseluruhan': total}
                dataBelanja.append(dataMakanan)
            elif pilihMakanan == "4":
                namaMakanan = "Mie Kuah"
                jenisMenu = "Makanan"
                porsiDipesan = porsi
                hargaMakanan = 10000
                totalSementara = hargaMakanan*porsi
                total += totalSementara
                dataMakanan = {'Tanggal Pesan': tanggal, 'Nama Pemesan': namaUser, 'Nama Menu': namaMakanan, 'Jenis Menu': jenisMenu,
                               'Porsi Dipesan': porsiDipesan, 'Harga': hargaMakanan, 'Total Sementara': totalSementara, 'Total Keseluruhan': total}
                dataBelanja.append(dataMakanan)
            elif pilihMakanan == "5":
                buatPesanan()
                break
            elif pilihMakanan == "0":
                exit(0)
            else:
                print("Menu Yang Anda Masukkan Salah!!")
                print("\n")
                input("Tekan Enter Untuk Memasukkan Kembali...")
                makanan()
        elif command == 't':
            backToPesanan()
            break
        else:
            print("Karakter Yang Anda Masukkan Salah!!!")
            input("Tekan Enter Untuk Lanjut...")
            makanan()

        command = input(
            "Apakah Anda Ingin Memesan Makanan Lagi?[y/t]: ").lower()


def minuman():
    hapusLayar()
    command = 'y'
    global namaUser
    global total
    while True:
        if command == 'y':
            print("{0:^50}".format("Welcome To RESTECHNO"))
            print("{0:^50}".format("Silahkan Memilih Minuman Yang Akan Dipesan"))
            print("-" * 50)
            for data in dataUser:
                print(f"Nama User: {data['nama']}",
                      " "*13, f"Tanggal: {tanggal}")
                namaUser = data['nama']
            print("-" * 50)
            print("[1] Es Teh - Rp. 2.000")
            print("[2] Es Jeruk - Rp. 3.500")
            print("[3] Kopi - Rp. 4.000")
            print("[4] Joshua - Rp. 5.000")
            print("[5] Kembali")
            print("[0] Exit")
            print("-"*50)
            pilihMinuman = input("Pilih Minuman=> ")
            porsi = int(input("Porsi Yang Dipesan: "))

            if pilihMinuman == "1":
                namaMinuman = "Es Teh"
                jenisMenu = "Minuman"
                porsiDipesan = porsi
                hargaMinuman = 2000
                totalSementara = hargaMinuman*porsi
                total += totalSementara
                dataMinuman = {'Tanggal Pesan': tanggal, 'Nama Pemesan': namaUser, 'Nama Menu': namaMinuman, 'Jenis Menu': jenisMenu,
                               'Porsi Dipesan': porsiDipesan, 'Harga': hargaMinuman, 'Total Sementara': totalSementara, 'Total Keseluruhan': total}
                dataBelanja.append(dataMinuman)
            elif pilihMinuman == "2":
                namaMinuman = "Es Jeruk"
                jenisMenu = "Minuman"
                porsiDipesan = porsi
                hargaMinuman = 3500
                totalSementara = hargaMinuman*porsi
                total += totalSementara
                dataMinuman = {'Tanggal Pesan': tanggal, 'Nama Pemesan': namaUser, 'Nama Menu': namaMinuman, 'Jenis Menu': jenisMenu,
                               'Porsi Dipesan': porsiDipesan, 'Harga': hargaMinuman, 'Total Sementara': totalSementara, 'Total Keseluruhan': total}
                dataBelanja.append(dataMinuman)
            elif pilihMinuman == "3":
                namaMinuman = "Kopi"
                jenisMenu = "Minuman"
                porsiDipesan = porsi
                hargaMinuman = 4000
                totalSementara = hargaMinuman*porsi
                total += totalSementara
                dataMinuman = {'Tanggal Pesan': tanggal, 'Nama Pemesan': namaUser, 'Nama Menu': namaMinuman, 'Jenis Menu': jenisMenu,
                               'Porsi Dipesan': porsiDipesan, 'Harga': hargaMinuman, 'Total Sementara': totalSementara, 'Total Keseluruhan': total}
                dataBelanja.append(dataMinuman)
            elif pilihMinuman == "4":
                namaMinuman = "Joshua"
                jenisMenu = "Minuman"
                porsiDipesan = porsi
                hargaMinuman = 5000
                totalSementara = hargaMinuman*porsi
                total += totalSementara
                dataMinuman = {'Tanggal Pesan': tanggal, 'Nama Pemesan': namaUser, 'Nama Menu': namaMinuman, 'Jenis Menu': jenisMenu,
                               'Porsi Dipesan': porsiDipesan, 'Harga': hargaMinuman, 'Total Sementara': totalSementara, 'Total Keseluruhan': total}
                dataBelanja.append(dataMinuman)
            elif pilihMinuman == "5":
                buatPesanan()
                break
            elif pilihMinuman == "0":
                exit(0)
            else:
                print("Menu Yang Anda Masukkan Salah!!")
                print("\n")
                input("Tekan Enter Untuk Memasukkan Kembali...")
                makanan()
        elif command == 't':
            backToPesanan()
            break
        else:
            print("Karakter Yang Anda Masukkan Salah!!!")
            input("Tekan Enter Untuk Lanjut...")
            makanan()
        command = input(
            "Apakah Anda Ingin Memesan Makanan Lagi?[y/t]: ").lower()


def keranjang():
    hapusLayar()
    print("{0:^50}".format("Welcome To RESTECHNO"))
    print("{0:^50}".format("Silahkan Memilih Menu Yang Ditampilkan"))
    print("-" * 50)
    for data in dataUser:
        print(f"Nama User: {data['nama']}", " "*13, f"Tanggal: {tanggal}")
    print("-" * 50)
    print("[1] Lihat Keranjang")
    print("[2] Hapus Makanan/Minuman Yang Dipesan")
    print("[3] Kembali")
    print("[0] Exit")
    print("-" * 50)
    pilihMenu = input("Pilih Menu=> ")

    if pilihMenu == "1":
        lihatKeranjang()
    elif pilihMenu == "2":
        hapusBarang()
    elif pilihMenu == "3":
        buatPesanan()
    elif pilihMenu == "0":
        exit(0)
    else:
        print("Menu Yang Anda Masukkan Salah")
        backToPesanan()


def lihatKeranjang():
    hapusLayar()
    print("{0:^105}".format("Welcome To RESTECHNO"))
    print("{0:^105}".format("List Belanja Anda Akan Ditampung Disini"))
    print("-" * 105)
    for data in dataUser:
        print(f"Nama User: {data['nama']}",
              " "*13, f"Tanggal: {tanggal}")
    print("-" * 105)
    if len(dataBelanja) > 0:
        print("{0:^90}".format(
            "Nama Menu \t Jenis Menu \t Porsi Dipesan \t Harga \t Total Sementara \t Total Keseluruhan"))
        print("-"*105)
        for data in dataBelanja:
            print("{0:^50}".format(
                f"{data['Nama Menu']} \t {data['Jenis Menu']} \t\t {data['Porsi Dipesan']} \t {data['Harga']} \t\t {data['Total Sementara']} \t\t {data['Total Keseluruhan']}"))
        command = input("Apakah Anda Ingin Checkout?[y/t]: ").lower()
        if command == 'y':
            checkout()
        elif command == 't':
            keranjang()
        else:
            print("Menu Yang Anda Masukkan Salah!!")
            print("\n")
            input("Tekan Enter Untuk Memasukkan Kembali...")
            lihatKeranjang()
    else:
        print("Tidak Ada Data")
        backToPesanan()


def hapusBarang():
    hapusLayar()
    print("{0:^105}".format("Welcome To RESTECHNO"))
    print("{0:^105}".format("List Belanja Anda Akan Ditampung Disini"))
    print("-" * 105)
    for data in dataUser:
        print(f"Nama User: {data['nama']}",
              " "*13, f"Tanggal: {tanggal}")
    print("-" * 105)
    if len(dataBelanja) > 0:
        print("{0:^90}".format(
            "No. \t Nama Menu \t Jenis Menu \t Porsi Dipesan \t Harga \t Total Sementara \t Total Keseluruhan"))
        print("-"*105)
        i = 1
        for data in dataBelanja:
            print("{0:^50}".format(
                f"{i} \t {data['Nama Menu']} \t {data['Jenis Menu']} \t\t {data['Porsi Dipesan']} \t {data['Harga']} \t\t {data['Total Sementara']} \t\t {data['Total Keseluruhan']}"))
            i += 1
        print("\n")
        print("-"*50)
        hapus = int(input("Masukkan Nomor Barang Yang Ingin Dihapus: "))
        dataBelanja.pop(hapus-1)

        print("Barang Berhasil Dihapus")
        print("\n")
        input("Tekan Enter Untuk Lanjut...")
        keranjang()

    else:
        print("Tidak Ada Data")
        backToPesanan()


def batalkanPesanan():
    global total
    hapusLayar()
    print("{0:^50}".format("Welcome To RESTECHNO"))
    print("{0:^50}".format("List Belanja Anda Akan Ditampung Disini"))
    print("-" * 50)
    for data in dataUser:
        print(f"Nama User: {data['nama']}",
              " "*37, f"Tanggal: {tanggal}")
    print("-"*50)
    print("\n")
    command = input("Anda Yakin Ingin Membatalkan Pesanan?[y/t]: ").lower()
    if command == 'y':
        print("Membatalkan Pesanan...")
        time.sleep(3)
        dataBelanja.clear()
        total = 0
        print("Pesanan Berhasil Dibatalkan!!")
        print("\n")
        input("Tekan Enter Untuk Lanjut...")
        buatPesanan()
    elif command == 't':
        print("\n")
        input("Tekan Enter Untuk Lanjut...")
        buatPesanan()
    else:
        print("Karakter Yang Anda Masukkan Salah!!")
        print("\n")
        input("Tekan Enter Untuk Lanjut...")
        batalkanPesanan()


def checkout():
    global total
    hapusLayar()
    print("{0:^73}".format("Welcome To RESTECHNO"))
    print("{0:^73}".format("List Belanja Anda Akan Ditampung Disini"))
    print("-" * 73)
    for data in dataUser:
        print(f"Nama User: {data['nama']}",
              " "*37, f"Tanggal: {tanggal}")
    if len(dataBelanja) > 0:
        print("-"*73)
        print("{0:^50}".format(
            "Nama Menu \t Jenis Menu \t Porsi Dipesan \t Harga \t Total Sementara"))
        print("-"*73)
        for data in dataBelanja:
            print("{0:^50}".format(
                f"{data['Nama Menu']} \t {data['Jenis Menu']} \t\t {data['Porsi Dipesan']} \t {data['Harga']} \t\t {data['Total Sementara']}"))
        print("-"*73)
        print("{0:^73}".format(f"Total Yang Harus Dibayar: {total}"))
        print("-"*73)
        command = input("Apakah Anda Ingin Checkout?[y/t]: ").lower()
        if command == 'y':
            bayar = int(input("Masukkan Jumlah Uang Yang Dibayarkan: "))
            if bayar >= total:
                kembalian = bayar - total
                print("Kembalian Anda: Rp.", '{:,}'.format(kembalian))
                try:
                    with open(fileBelanja, 'r') as csvfile:
                        csv.reader(csvfile, delimiter=',')
                    simpanBelanja()

                except IOError:
                    namaKolom = ['Tanggal Pesan', 'Nama Pemesan', 'Nama Menu', 'Jenis Menu',
                                 'Porsi Dipesan', 'Harga', 'Total Sementara', 'Total Keseluruhan']

                    with open(fileBelanja, 'w', newline='') as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=namaKolom)
                        writer.writeheader()
                        writer.writerows(dataBelanja)
                    print('Sedang Memproses Pesanan....')
                    time.sleep(4)
                    dataBelanja.clear()
                    total = 0
                    print("Pesanan Tersimpan!!!")
                    backToPesanan()
            else:
                print("Uang Anda Kurang")
                print("\n")
                input("Tekan Enter Untuk Lanjut...")
                checkout()
        elif command == 't':
            buatPesanan()
        else:
            print("Karakter Yang Anda Masukkan Salah!!!")
            print("\n")
            input("Tekan Enter Untuk Lanjut...")
            checkout()

    else:
        print("Tidak Ada Data!!!")
        print("\n")
        input("Tekan Enter Untuk Lanjut...")
        buatPesanan()


def simpanBelanja():
    global total
    namaKolom = ['Tanggal Pesan', 'Nama Pemesan', 'Nama Menu', 'Jenis Menu',
                 'Porsi Dipesan', 'Harga', 'Total Sementara', 'Total Keseluruhan']

    with open(fileBelanja, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=namaKolom)
        for data in dataBelanja:
            writer.writerow(data)

    print('Sedang Memproses Pesanan....')
    time.sleep(4)
    dataBelanja.clear()
    total = 0
    backToPesanan()


def lihatRiwayatPesanan():
    hapusLayar()
    penampung = []
    riwayat = []
    print("{0:^50}".format("Welcome To RESTECHNO"))
    print("{0:^50}".format("Berikut Adalah List Riwayat Pesanan Anda"))
    print("-" * 50)
    for data in dataUser:
        print(f"Nama User: {data['nama']}",
              " "*13, f"Tanggal: {tanggal}")
        namaUser = data['nama']
    print("-" * 50)
    try:
        with open(fileBelanja, 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for data in reader:
                penampung.append(data)

            for data in penampung:
                if data['Nama Pemesan'] == namaUser:
                    riwayat.append(data)

            if len(riwayat) > 0:
                print("-"*105)
                print("{0:^90}".format(
                    "No. \t Tanggal Pesan \t Nama Pemesan \t Nama Menu \t Porsi Dipesan \t Harga \t Total Sementara \t Total Keseluruhan"))
                print("-"*105)
                i = 1
                for data in riwayat:
                    print("{0:^50}".format(
                        f"{i} \t {data['Tanggal Pesan']} \t {data['Nama Pemesan']} \t\t {data['Nama Menu']} \t\t {data['Porsi Dipesan']} \t {data['Harga']} \t\t {data['Total Sementara']} \t\t {data['Total Keseluruhan']} \t"))
                    i += 1
                print('-'*50)
                print('\n')
                input("Tekan Enter Untuk Lanjut...")
                riwayatTransaksi()
            else:
                print("Tidak Ada Data")
                print('\n')
                input("Tekan Enter Untuk Lanjut...")
                riwayatTransaksi()
    except IOError:
        print("Anda Belum Pernah Melakukan Pemesanan!!!")
        print('\n')
        input("Tekan Enter Untuk Lanjut...")
        riwayatTransaksi()


def hapusRiwayatPesanan():
    hapusLayar()
    namaKolom = ['Tanggal Pesan', 'Nama Pemesan', 'Nama Menu', 'Jenis Menu',
                 'Porsi Dipesan', 'Harga', 'Total Sementara', 'Total Keseluruhan']
    penampung = []
    riwayat = []
    print("{0:^50}".format("Welcome To RESTECHNO"))
    print("{0:^50}".format("Berikut Adalah List Riwayat Pesanan Anda"))
    print("-" * 50)
    for data in dataUser:
        print(f"Nama User: {data['nama']}",
              " "*13, f"Tanggal: {tanggal}")
        namaUser = data['nama']
    print("-" * 50)
    try:
        with open(fileBelanja, 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for data in reader:
                penampung.append(data)

            for data in penampung:
                if data['Nama Pemesan'] == namaUser:
                    riwayat.append(data)

            if len(riwayat) > 0:
                print("-"*105)
                print("{0:^90}".format(
                    "No. \t Tanggal Pesan \t Nama Pemesan \t Nama Menu \t Porsi Dipesan \t Harga \t Total Sementara \t Total Keseluruhan"))
                print("-"*105)
                i = 1
                for data in riwayat:
                    print("{0:^50}".format(
                        f"{i} \t {data['Tanggal Pesan']} \t {data['Nama Pemesan']} \t\t {data['Nama Menu']} \t\t {data['Porsi Dipesan']} \t {data['Harga']} \t\t {data['Total Sementara']} \t\t {data['Total Keseluruhan']} \t"))
                    i += 1
                print('-'*50)
                print('\n')
                lineDihapus = int(
                    input("Masukkan Nomor Urut Data Yang Ingin Dihapus: "))

                riwayat.pop(lineDihapus-1)

                try:
                    with open(fileBelanja, 'w', newline="") as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=namaKolom)
                        writer.writeheader()
                        writer.writerows(riwayat)

                    print("Menhapus Data...")
                    time.sleep(3)
                    print("Berhasil Menghapus Data!!!")
                    print("\n")
                    input("Tekan Enter Untuk Melihat Riwayat Transaksi...")
                    lihatRiwayatPesanan()
                except:
                    print("Tidak Ada Data!!!")
                    print("\n")
                    input("Tekan Enter Untuk Lanjut...")
                    riwayatTransaksi()
            else:
                print("Tidak Ada Data")
                print('\n')
                input("Tekan Enter Untuk Lanjut...")
                riwayatTransaksi()
    except IOError:
        print("Anda Belum Pernah Melakukan Pemesanan!!!")
        print('\n')
        input("Tekan Enter Untuk Lanjut...")
        riwayatTransaksi()


def profile():
    hapusLayar()
    print("{0:^50}".format("Welcome To RESTECHNO"))
    print("{0:^50}".format("Berikut Adalah Profile Anda"))
    print("-" * 50)
    for data in dataUser:
        print("{0:^50}".format(f"Nama : {data['nama']}"))
        print("{0:^50}".format(f"Username : {data['username']}"))
        print("{0:^50}".format(f"Tanggal Lahir : {data['tglLahir']}"))
        print("{0:^50}".format(f"Alamat : {data['alamat']}"))
        print("{0:^50}".format(f"Tanggal Daftar : {data['tglDaftar']}"))
    print("-"*50)
    print("\n")
    input("Tekan Enter Untuk Lanjut....")
    mainMenu()


def hapusAkun():
    hapusLayar()
    listUser = []
    userDihapus = []
    penampung = []
    header = ['nama', 'username',
              'password', 'tglLahir', 'alamat', 'tglDaftar']

    command = input(
        "Apakah Anda Yakin Ingin Menghapus Akun Ini?[y/t]: ").lower()
    if command == 'y':
        print("{0:^50}".format("Silahkan Login Kembali Untuk Mengkonfirmasi!!"))
        username = input("Username: ")
        password = input("Password: ")
        with open(fileUser, 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for data in reader:
                listUser.append(data)

        for data in listUser:
            if username == data['username'] and password == data['password']:
                userDihapus.append(data)
            else:
                penampung.append(data)
                continue

        if len(userDihapus) > 0:
            with open(fileUser, 'w', newline="") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=header)
                writer.writeheader()
                writer.writerows(penampung)

            print("Menghapus Akun...")
            time.sleep(3)
            print("Akun Berhasil Dihapus...")
            print("\n")
            input("Tekan Enter Untuk Lanjut...")
            dataUser.clear()
            launcher()
        else:
            print("Username/Password Yang Anda Masukkan Salah!!!")
            print("\n")
            input("Tekan Enter Untuk Mengkonfirmasi Kembali...")
            hapusAkun()


if __name__ == "__main__":
    while True:
        launcher()
