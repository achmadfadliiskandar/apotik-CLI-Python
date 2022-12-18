import mysql.connector
import showpembelian as pembelian
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="apotek"
)
pembelian
def deletepembelian():
    cursor = db.cursor()
    id = input("ketikan id user yang ingin di hapus : ")
    sql = "DELETE FROM pembelian WHERE id=%s"
    value = (id,)
    cursor.execute(sql,value)
    db.commit()
    print("data berhasil di hapus")
deletepembelian()