import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="apotek"
)
def showbarang():
    print("data barang")
    cursor = db.cursor()
    sql = "SELECT * FROM barang"
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount == 0:
        print("data kosong")
    else:
        for data in result:
            print(data)
showbarang()