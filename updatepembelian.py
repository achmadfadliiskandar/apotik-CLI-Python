import mysql.connector
import random
import showpetugas as tugas
import showpembelian as pembelian
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
pembelian
# untuk mengupdate tugas di database apotek
def updatepembelian():
    # tugas.showdata()
    cursor = db.cursor()
    id = input("pilih id Pembelian : ")
    nama_pembeli = input("Masukan Nama Pembeli : ")
    id_petugas = input("Masukan Id Petugas : ")
    id_barang = input("Masukan Id Barang : ")
    id_tugas = input("Masukan Id Tugas : ")
    qty = input("Masukan Jumlah Pembelian : ")
    # kode_unik = random.randint(1000,10000)
    value = (nama_pembeli,id_petugas,id_barang,id_tugas,qty,id)
    sql = "UPDATE pembelian SET nama_pembeli=%s,id_petugas=%s,id_barang=%s,id_tugas=%s,qty=%s WHERE id=%s"
    cursor.execute(sql,value)
    db.commit()
    print('data berhasil di Update')
updatepembelian()
