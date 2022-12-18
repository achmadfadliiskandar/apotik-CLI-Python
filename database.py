import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="apotek"
)
# ini buat pengecekan kalau databasenya berhasil connect

# if db.is_connected:
#     print("database berhasil disambungkan")

# untuk menambahkan tugas di database apotek
# def storedata():
#     hari = input("Masukan Hari Tugas : ")
#     waktu_mulai = input("Masukan Waktu Mulai Tugas : ")
#     waktu_selesai = input("Masukan Waktu Selesai Tugas : ")
#     value = (hari,waktu_mulai,waktu_selesai)
#     cursor = db.cursor()
#     sql = "INSERT INTO tugas (hari,waktu_mulai,waktu_selesai) VALUES (%s,%s,%s)"
#     cursor.execute(sql,value)
#     db.commit()
#     print("data berhasil di tambah")
# storedata()