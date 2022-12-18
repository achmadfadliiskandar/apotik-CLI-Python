import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="apotek"
)
def showdata():
    print("jadwal tugas")
    cursor = db.cursor()
    sql = "SELECT * FROM tugas"
    cursor.execute(sql)

    results = cursor.fetchall()

    if cursor.rowcount == 0:
        print("data kosong")
    else:
        for data in results:
            print(data)
showdata()
