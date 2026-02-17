class Kasir:
    def __init__(self):
        self.daftar_barang = {}
        self.keranjang = {}

    def tambah_barang(self, nama, harga):
        self.daftar_barang[nama] = harga

    def hapus_barang(self, nama):
        if nama in self.daftar_barang:
            del self.daftar_barang[nama]
        else:
            print("Barang tidak ditemukan.")

    def tampilkan_daftar_barang(self):
        print("Daftar Barang:")
        for nama, harga in self.daftar_barang.items():
            print(f"{nama}: Rp {harga}")

    def tambah_ke_keranjang(self, nama, jumlah):
        if nama in self.daftar_barang:
            if nama in self.keranjang:
                self.keranjang[nama] += jumlah
            else:
                self.keranjang[nama] = jumlah
        else:
            print("Barang tidak ditemukan.")

    def hapus_dari_keranjang(self, nama, jumlah):
        if nama in self.keranjang:
            if self.keranjang[nama] > jumlah:
                self.keranjang[nama] -= jumlah
            elif self.keranjang[nama] == jumlah:
                del self.keranjang[nama]
            else:
                print("Jumlah yang dihapus melebihi jumlah di keranjang.")
        else:
            print("Barang tidak ditemukan di keranjang.")

    def tampilkan_keranjang(self):
        print("Keranjang:")
        for nama, jumlah in self.keranjang.items():
            print(f"{nama}: {jumlah} x Rp {self.daftar_barang[nama]}")

    def hitung_total(self):
        total = 0
        for nama, jumlah in self.keranjang.items():
            total += jumlah * self.daftar_barang[nama]
        return total

def main():
    kasir = Kasir()

    while True:
        print("\nMenu:")
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Tampilkan Daftar Barang")
        print("4. Tambah ke Keranjang")
        print("5. Hapus dari Keranjang")
        print("6. Tampilkan Keranjang")
        print("7. Hitung Total")
        print("8. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input("Masukkan nama barang: ")
            harga = int(input("Masukkan harga barang: "))
            kasir.tambah_barang(nama, harga)
        elif pilihan == "2":
            nama = input("Masukkan nama barang: ")
            kasir.hapus_barang(nama)
        elif pilihan == "3":
            kasir.tampilkan_daftar_barang()
        elif pilihan == "4":
            nama = input("Masukkan nama barang: ")
            jumlah = int(input("Masukkan jumlah barang: "))
            kasir.tambah_ke_keranjang(nama, jumlah)
        elif pilihan == "5":
            nama = input("Masukkan nama barang: ")
            jumlah = int(input("Masukkan jumlah barang: "))
            kasir.hapus_dari_keranjang(nama, jumlah)
        elif pilihan == "6":
            kasir.tampilkan_keranjang()
        elif pilihan == "7":
            print(f"Total: Rp {kasir.hitung_total()}")
        elif pilihan == "8":
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()