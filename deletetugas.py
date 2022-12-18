import mysql.connector
import showtugas as tugas
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="apotek"
)
tugas
def deletedata():
    cursor = db.cursor()
    id = input("ketikan id user yang ingin di hapus : ")
    sql = "DELETE FROM tugas WHERE id=%s"
    value = (id,)
    cursor.execute(sql,value)
    db.commit()
    print("data berhasil di hapus")
deletedata()