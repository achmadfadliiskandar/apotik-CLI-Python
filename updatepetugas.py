import mysql.connector
import showpetugas as petugas
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="apotek"
)
petugas
# untuk mengupdate tugas di database apotek
def updatedata():
    # tugas.showdata()
    cursor = db.cursor()
    id = input("pilih id Barang : ")
    nama_petugas = input("Masukan Nama Petugas : ")
    email_petugas = input("Masukan Email Petugas : ")
    nomor_petugas = input("Masukan Nomor Petugas : ")
    sql = "UPDATE petugas SET nama_petugas=%s,email_petugas=%s,nomor_petugas=%s WHERE id=%s"
    value = (nama_petugas,email_petugas,nomor_petugas,id)
    cursor.execute(sql,value)
    db.commit()
    print('data berhasil di Update')
updatedata()
