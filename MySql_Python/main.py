from services import db

def tambahBarang():
    kode_barang = input("Kode barang : ")
    nama_barang = input("Nama barang : ")
    harga_barang = int(input("Harga barang : "))
    stok_barang = int(input("Stok barang : "))

    db.tambahItem(kode_barang, nama_barang, harga_barang, stok_barang)

def cekBarang():
    daftarBarang = db.cekItem()
    print("\t\nDaftar Barang :")
    for kolom in daftarBarang:
        print("\t\nkode", kolom[1], " | ", kolom[2], " | Rp ", kolom[3], " | stok: ", kolom[4])

def updateBarang():
    nama_barang = input("Nama barang (barang mana yang mau diubah?): ")
    kode_barang = input("Kode barang baru : ")
    harga_barang = int(input("Harga barang baru : "))
    stok_barang = int(input("Stok barang baru : "))

    db.updateItem(kode_barang, harga_barang, stok_barang, nama_barang)
    print("\nBerhasil diubah! \n\n Daftar barang saat ini:")
    cekBarang()
    
def hapusBarang():
    nama_barang = input("Nama barang (barang mana yang mau dihapus?): ")
    yakin = input("\nYakin ingin menghapusnya? (y/n):\n")
    if yakin == "y":
        db.hapusItem(nama_barang)
        print("\nBerhasil dihapus")
    elif yakin == "n":
        print("\nDibatalkan")
    else:
        print("\nInput gak valid")
while True:
    print("="*20)
    print("SELAMAT DATANG DI TOKO SERBASERBA\n\n")
    print("1. Tambah barang")
    print("2. Cek barang")
    print("3. Update barang")
    print("4. Hapus barang")
    print("5. Keluar")

    pilihan = int(input("Pilih menu (1/2/3/4/5):"))

    if pilihan == 1 :
        tambahBarang()
    elif pilihan == 2 :
        cekBarang()
    elif pilihan == 3 :
        updateBarang()
    elif pilihan == 4 :
        hapusBarang()
    elif pilihan == 5 :
        break
    else :
        print("Pilihan gak valid")