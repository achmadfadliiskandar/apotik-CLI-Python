import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="apotek"
)
# untuk menambahkan PETUGAS di database apotek
def storedata():
    nama_petugas = input("Masukan Nama Petugas : ")
    email_petugas = input("Masukan Email Petugas : ")
    nomor_petugas = input("Masukan Nomor Petugas : ")
    value = (nama_petugas,email_petugas,nomor_petugas)
    cursor = db.cursor()
    sql = "INSERT INTO petugas (nama_petugas,email_petugas,nomor_petugas) VALUES (%s,%s,%s)"
    cursor.execute(sql,value)
    db.commit()
    print("data berhasil di tambah")
storedata()
