class Nasabah:
    def __init__(self, nama, alamat, no_telp):
        self.nama = nama
        self.alamat = alamat
        self.no_telp = no_telp

class Rekening:
    def __init__(self, no_rek, saldo):
        self.no_rek = no_rek
        self.saldo = saldo
        self.nasabah = None

    def tambah_nasabah(self, nasabah):
        self.nasabah = nasabah

class Bank:
    def __init__(self, nama_bank):
        self.nama_bank = nama_bank
        self.daftar_rekening = []

    def buka_rekening(self, no_rek, saldo, nasabah):
        rekening = Rekening(no_rek, saldo)
        rekening.tambah_nasabah(nasabah)
        self.daftar_rekening.append(rekening)
        print(f"Rekening {no_rek} berhasil dibuka.")

    def tampilkan_rekening(self):
        for rekening in self.daftar_rekening:
            print(f"No. Rekening: {rekening.no_rek}")
            print(f"Nama Nasabah: {rekening.nasabah.nama}")
            print(f"Alamat: {rekening.nasabah.alamat}")
            print(f"No. Telp: {rekening.nasabah.no_telp}")
            print(f"Saldo: {rekening.saldo}")
            print("------------------------")

bank = Bank("BRI")
while True:
    print("1. Buka Rekening")
    print("2. Tampilkan Rekening")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        nama = input("Masukkan nama nasabah: ")
        alamat = input("Masukkan alamat nasabah: ")
        no_telp = input("Masukkan no. telp nasabah: ")
        no_rek = input("Masukkan no. rekening: ")
        saldo = int(input("Masukkan saldo awal: "))
        nasabah = Nasabah(nama, alamat, no_telp)
        bank.buka_rekening(no_rek, saldo, nasabah)
    elif pilihan == "2":
        bank.tampilkan_rekening()
    elif pilihan == "3":
        break
    else:
        print("Pilihan tidak valid.")