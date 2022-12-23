import mysql.connector
import pandas as pd
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
    # added data in csv
    data = result
    df = pd.DataFrame(data)
    df.to_csv('data.csv', mode='a', index=False, header=False)
    print("Laporan Added")
    # added data in csv
    if cursor.rowcount == 0:
        print("data kosong")
    else:
        for data in result:
            print(data)
showpetugas()