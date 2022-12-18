import mysql.connector
import random
import showpetugas as tugas
import showbarang as barang
import showtugas as tgs
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="apotek"
)
tugas
barang
tgs
# untuk menambahkan PEMBELIAN di database apotek
def storepembeli():
    nama_pembeli = input("Masukan Nama Pembeli : ")
    id_petugas = input("Masukan Id Petugas : ")
    id_barang = input("Masukan Id Barang : ")
    id_tugas = input("Masukan Id Tugas : ")
    qty = input("Masukan Jumlah Pembelian : ")
    kode_unik = random.randint(1000,10000)
    value = (nama_pembeli,id_petugas,id_barang,id_tugas,qty,kode_unik)
    cursor = db.cursor()
    sql = "INSERT INTO pembelian (nama_pembeli,id_petugas,id_barang,id_tugas,qty,kode_unik) VALUES (%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql,value)
    db.commit()
    print("data berhasil di tambah")
storepembeli()
