import mysql.connector as mysql
from mysql.connector import Error

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "keuangan",
}

def get_conn():
    return mysql.connect(**DB_CONFIG)

def inputPemasukan(jumlah, keterangan, tanggal):
    conn = None
    try:
        conn = get_conn()
        cursor = conn.cursor()
        sql = ("INSERT INTO inputpemasukan "
               "(jumlah_pemasukan, keterangan_pemasukan, tanggal_pemasukan) "
               "VALUES (%s, %s, %s)")
        cursor.execute(sql, (int(jumlah), keterangan, tanggal))
        conn.commit()
    except Error as e:
        if conn:
            conn.rollback()
        raise
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def inputPengeluaran(jumlah, keterangan, tanggal):
    conn = None
    try:
        conn = get_conn()
        cursor = conn.cursor()
        sql = ("INSERT INTO inputpengeluaran "
               "(jumlah_pengeluaran, keterangan_pengeluaran, tanggal_pengeluaran) "
               "VALUES (%s, %s, %s)")
        cursor.execute(sql, (int(jumlah), keterangan, tanggal))
        conn.commit()
    except Error as e:
        if conn:
            conn.rollback()
        raise
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
