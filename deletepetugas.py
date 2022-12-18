import mysql.connector
import showpetugas as petugas
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="apotek"
)
petugas
def deletepetugas():
    cursor = db.cursor()
    id = input("ketikan id petugas yang ingin di hapus : ")
    sql = "DELETE FROM petugas WHERE id=%s"
    value = (id,)
    cursor.execute(sql,value)
    db.commit()
    print("data berhasil di hapus")
deletepetugas()