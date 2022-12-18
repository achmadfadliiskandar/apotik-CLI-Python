import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "apotek"
)
def showpembelian():
    print("pembelian")
    cursor = db.cursor()
    sql = "SELECT pembelian.id, pembelian.nama_pembeli, petugas.nama_petugas, barang.nama_barang,barang.hargabarang,pembelian.qty,barang.hargabarang*pembelian.qty as totalharga,tugas.hari FROM (((pembelian INNER JOIN petugas ON pembelian.id_petugas = petugas.id) INNER JOIN barang ON pembelian.id_barang = barang.id) INNER JOIN tugas on pembelian.id_tugas = tugas.id);"
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount == 0:
        print("data kosong")
    else:
        for i in result:
            print(i)
showpembelian()
# tolong simpan dulu bos
# SELECT pembelian.id, pembelian.nama_pembeli, petugas.nama_petugas, barang.nama_barang,barang.hargabarang,pembelian.qty,barang.hargabarang*pembelian.qty as totalharga,tugas.hari 
# FROM (((pembelian INNER JOIN petugas ON pembelian.id_petugas = petugas.id) 
# INNER JOIN barang ON pembelian.id_barang = barang.id) 
# INNER JOIN tugas on pembelian.id_tugas = tugas.id);
# jangan sampai ada yang salah bos karena jika salah maka nggak jalan