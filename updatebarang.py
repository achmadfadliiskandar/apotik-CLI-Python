import mysql.connector
import showbarang as barang
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="apotek"
)
barang
# untuk mengupdate tugas di database apotek
def updatedata():
    # tugas.showdata()
    cursor = db.cursor()
    id = input("pilih id Barang : ")
    nama_barang = input("Masukan Nama Barang : ")
    hargabarang = input("Masukan Harga Barang : ")
    stok = input("Masukan Stok Barang : ")
    expired = input("Masukan Tanggal Expired Barang : ")
    sql = "UPDATE barang SET nama_barang=%s,hargabarang=%s,stok=%s,expired=%s WHERE id=%s"
    value = (nama_barang,hargabarang,stok,expired,id)
    cursor.execute(sql,value)
    db.commit()
    print('data berhasil di Update')
updatedata()
