import mysql.connector
import showbarang as barang
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="apotek"
)
barang
def deletebarang():
    cursor = db.cursor()
    id = input("ketikan id user yang ingin di hapus : ")
    sql = "DELETE FROM barang WHERE id=%s"
    value = (id,)
    cursor.execute(sql,value)
    db.commit()
    print("data berhasil di hapus")
deletebarang()