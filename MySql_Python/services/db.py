import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "latihantoko",
)

def tambahItem(kode_barang, nama_barang, harga_barang, stok_barang):
    cursor = db.cursor()
    cursor.execute("INSERT INTO tabelbarang (kode_barang, nama_barang, harga_barang, stok_barang) VALUES (%s, %s, %s, %s)", (kode_barang, nama_barang, harga_barang, stok_barang))

    db.commit()

    if cursor.rowcount > 0:
        return print("\nBarang sudah di catat!\n")
    else:
        print("\nBarang gagal ditambahkan!\n")

    cursor.close()

def cekItem():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tabelbarang")
    return cursor.fetchall()

def updateItem(kode_barang, harga_barang, stok_barang, nama_barang):
    cursor = db.cursor()
    cursor.execute("UPDATE tabelbarang SET kode_barang = %s, harga_barang = %s, stok_barang = %s WHERE nama_barang = %s", (kode_barang, harga_barang, stok_barang, nama_barang))

    db.commit()
    cursor.close()


def hapusItem(nama_barang):
    cursor = db.cursor()
    cursor.execute("DELETE FROM tabelbarang WHERE nama_barang = %s", (nama_barang,))

    db.commit()
    cursor.close()


    