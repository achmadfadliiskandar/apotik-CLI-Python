import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="apotek"
)
# untuk menambahkan BARANG di database apotek
def storedata():
    nama_barang = input("Masukan Nama Barang : ")
    harga_barang = input("Masukan Harga Barang : ")
    stok = input("Masukan Stok Barang : ")
    expired = input("Masukan Tanggal Expired Barang : ")
    value = (nama_barang,harga_barang,stok,expired)
    cursor = db.cursor()
    sql = "INSERT INTO barang (nama_barang,hargabarang,stok,expired) VALUES (%s,%s,%s,%s)"
    cursor.execute(sql,value)
    db.commit()
    print("data berhasil di tambah")
storedata()
