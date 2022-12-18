import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "apotek"
)
def showpetugas():
    print("Data Petugas")
    cursor = db.cursor()
    sql = "SELECT * FROM petugas"
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount == 0:
        print("data kosong")
    else:
        for data in result:
            print(data)
showpetugas()