import mysql.connector
import pandas as pd
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
    # added data in csv
    data = results
    df = pd.DataFrame(data)
    df.to_csv('data.csv', mode='a', index=False, header=False)
    print("Laporan Added")
    # added data in csv
    if cursor.rowcount == 0:
        print("data kosong")
    else:
        for data in results:
            print(data)
showdata()
