import mysql.connector
import showtugas as tugas
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="apotek"
)
tugas
# untuk mengupdate tugas di database apotek
def updatedata():
    # tugas.showdata()
    cursor = db.cursor()
    id = input("pilih id Tugas : ")
    hari = input("Masukan Hari Tugas : ")
    waktu_mulai = input("Masukan Waktu Mulai Tugas : ")
    waktu_selesai = input("Masukan Waktu Selesai Tugas : ")
    sql = "UPDATE tugas SET hari=%s,waktu_mulai=%s,waktu_selesai=%s WHERE id=%s"
    value = (hari,waktu_mulai,waktu_selesai,id)
    cursor.execute(sql,value)
    db.commit()
    print('data berhasil di Update')
updatedata()
