# ini mah coba-coba dlu ya
# nanti kita nggak tau jadi nya gmn
# import database
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="apotek"
)
import showbarang
import showpetugas
import showtugas
import showpembelian
judulapdsk = "Apotik Anti Gedor 04" # judul aplikasi
print(str.upper(judulapdsk))
# isi_menu = int(input("Masukan Angka Yang Tertera Pada Menu Ini Ya : "))
print(
"""
MENU APLIKASI\n
1.JADWAL HARI TUGAS
2.MENU BARANG
3.NAMA-NAMA PETUGAS
4.BARANG YANG TERJUAL
5.LAPORAN PENJUALAN
6.MENAMBAHKAN HARI TUGAS
7.MENAMBAHKAN MENU BARANG
8.MENAMBAHKAN NAMA-NAMA PETUGAS
9.MENGUBAH HARI TUGAS
10.MENGUBAH MENU BARANG
11.MENGUBAH NAMA-NAMA PETUGAS
12.MENGHAPUS HARI TUGAS
13.MENGHAPUS MENU BARANG
14.MENGHAPUS NAMA-NAMA PETUGAS
15.KELUAR
"""
)
def menu():
    while True:
        try:
            isi_menu = int(input("Masukan Angka Yang Tertera Pada Menu Ini Ya : "))
        except:
            print('lanjut terus sampai benar')
            continue
        else:
            # ini fungsi untuk menghubungkan ke database
            if isi_menu == 1:
                print("Data Jadwal Tugas Apotik\n")
                showtugas.showdata()
                print("\n")
                print("INFO : JIKA INGIN KEMBALI KE MENU KETIKAN KELUAR/Keluar/keluar\n jika tidak mengetikan keyword / kata keluar maka aplikasi akan langsung keluar ke exit")
                menu_keluar = input("Apakah Ingin Kembali Ke Menu : ").lower()
                if menu_keluar == "keluar":
                    return menu()
                else:#perintah nya enter aja keluar aplikasi + dapat daata
                    print("hasil data")
                    showtugas.showdata()
            elif isi_menu == 2:
                print("Data Menu Barang Apotik\n")
                showbarang.showbarang()
                print("\n")
                print("INFO : JIKA INGIN KEMBALI KE MENU KETIKAN KELUAR/Keluar/keluar\n jika tidak mengetikan keyword / kata keluar maka aplikasi akan langsung keluar ke exit")
                menu_keluar = input("Apakah Ingin Kembali Ke Menu : ").lower()
                if menu_keluar == "keluar":
                    return menu()
                else:#perintah nya enter aja keluar aplikasi + dapat daata
                    print("hasil data")
                    showbarang.showbarang()
            elif isi_menu == 3:
                print("Data Petugas Apotik\n")
                showpetugas.showpetugas()
                print("\n")
                print("INFO : JIKA INGIN KEMBALI KE MENU KETIKAN KELUAR/Keluar/keluar\n jika tidak mengetikan keyword / kata keluar maka aplikasi akan langsung keluar ke exit")
                menu_keluar = input("Apakah Ingin Kembali Ke Menu : ").lower()
                if menu_keluar == "keluar":
                    return menu()
                else:#perintah nya enter aja keluar aplikasi + dapat daata
                    print("hasil data")
                    showpetugas.showpetugas()
            elif isi_menu == 4:
                print("Data Pembelian Apotik\n")
                showpembelian.showpembelian()
                print("\n")
                print("INFO : JIKA INGIN KEMBALI KE MENU KETIKAN KELUAR/Keluar/keluar\n jika tidak mengetikan keyword / kata keluar maka aplikasi akan langsung keluar ke exit")
                menu_keluar = input("Apakah Ingin Kembali Ke Menu : ").lower()
                if menu_keluar == "keluar":
                    return menu()
                else:#perintah nya enter aja keluar aplikasi + dapat daata
                    print("hasil data")
                    showpembelian.showpembelian()
            elif isi_menu == 5:
                print("Data Laporan Apotek\n")
                print("Data Pembelian")
                showpembelian.showpembelian()
                print("\n")
                print("Data Hari Tugas")
                showtugas.showdata()
                print("\n")
                print("Data Petugas")
                showpetugas.showpetugas()
                print("\n")
                print("Data Barang")
                showbarang.showbarang()
                print("\n")
                print("INFO : JIKA INGIN KEMBALI KE MENU KETIKAN KELUAR/Keluar/keluar\n jika tidak mengetikan keyword / kata keluar maka aplikasi akan langsung keluar ke exit")
                menu_keluar = input("Apakah Ingin Kembali Ke Menu : ").lower()
                if menu_keluar == "keluar":
                    return menu()
                else:#perintah nya enter aja keluar aplikasi + dapat daata
                    print("hasil data\nDan Anda Telah Keluar Dari aplikasi Terima kasih!!")
                    showpembelian.showpembelian()
            elif isi_menu == 6:
                def storedata():
                    # import database
                    hari = input("Masukan Hari Tugas : ")
                    waktu_mulai = input("Masukan Waktu Mulai Tugas : ")
                    waktu_selesai = input("Masukan Waktu Selesai Tugas : ")
                    value = (hari,waktu_mulai,waktu_selesai)
                    cursor = db.cursor()
                    sql = "INSERT INTO tugas (hari,waktu_mulai,waktu_selesai) VALUES (%s,%s,%s)"
                    cursor.execute(sql,value)
                    db.commit()
                    print("data berhasil di tambah")
                    menu_keluar = input("Apakah Ingin Kembali Ke Menu : ").lower()
                    if menu_keluar == "keluar":
                        return menu()
                    else:#perintah nya enter aja keluar aplikasi + dapat daata
                        print("hasil data\nDan Anda Telah Keluar Dari aplikasi Terima kasih!!")
                        showpembelian.showpembelian()
                storedata()
            elif isi_menu == 7:
                def storedata():
                    nama_barang = input("Masukan Nama Barang : ")
                    harga_barang = input("Masukan Harga Barang : ")
                    stok = input("Masukan Stok Barang : ")
                    expired = input("Masukan Tanggal Expired Barang : ")
                    value = (nama_barang,harga_barang,stok,expired)
                    cursor = db.cursor()
                    sql = "INSERT INTO barang (nama_barang,hargabarang,stok,expired) VALUES (%s,%s,%s,%s)"
                    cursor.execute(sql,value)
                    db.commit()
                    print("data berhasil di tambah")
                storedata()
                menu_keluar = input("Apakah Ingin Kembali Ke Menu : ").lower()
                if menu_keluar == "keluar":
                    return menu()
                else:#perintah nya enter aja keluar aplikasi + dapat daata
                    print("hasil data\nDan Anda Telah Keluar Dari aplikasi Terima kasih!!")
                    showpembelian.showpembelian()
            elif isi_menu == 8:
                def storedata():
                    nama_petugas = input("Masukan Nama Petugas : ")
                    email_petugas = input("Masukan Email Petugas : ")
                    nomor_petugas = input("Masukan Nomor Petugas : ")
                    value = (nama_petugas,email_petugas,nomor_petugas)
                    cursor = db.cursor()
                    sql = "INSERT INTO petugas (nama_petugas,email_petugas,nomor_petugas) VALUES (%s,%s,%s)"
                    cursor.execute(sql,value)
                    db.commit()
                    print("data berhasil di tambah")
                storedata()
                menu_keluar = input("Apakah Ingin Kembali Ke Menu : ").lower()
                if menu_keluar == "keluar":
                    return menu()
                else:#perintah nya enter aja keluar aplikasi + dapat daata
                    print("hasil data\nDan Anda Telah Keluar Dari aplikasi Terima kasih!!")
                    showpembelian.showpembelian()
            elif isi_menu == 9:
                showtugas.showdata()
                def updatedata():
                    # tugas.showdata()
                    cursor = db.cursor()
                    id = input("pilih id Tugas : ")
                    hari = input("Masukan Hari Tugas : ")
                    waktu_mulai = input("Masukan Waktu Mulai Tugas : ")
                    waktu_selesai = input("Masukan Waktu Selesai Tugas : ")
                    sql = "UPDATE tugas SET hari=%s,waktu_mulai=%s,waktu_selesai=%s WHERE id=%s"
                    value = (hari,waktu_mulai,waktu_selesai,id)
                    cursor.execute(sql,value)
                    db.commit()
                    print('data berhasil di Update')
                updatedata()
                menu_keluar = input("Apakah Ingin Kembali Ke Menu : ").lower()
                if menu_keluar == "keluar":
                    return menu()
                else:#perintah nya enter aja keluar aplikasi + dapat daata
                    print("hasil data\nDan Anda Telah Keluar Dari aplikasi Terima kasih!!")
                    showpembelian.showpembelian()
            elif isi_menu == 10:
                showbarang.showbarang()
                def updatedata():
                    # tugas.showdata()
                    cursor = db.cursor()
                    id = input("pilih id Barang : ")
                    nama_barang = input("Masukan Nama Barang : ")
                    hargabarang = input("Masukan Harga Barang : ")
                    stok = input("Masukan Stok Barang : ")
                    expired = input("Masukan Tanggal Expired Barang : ")
                    sql = "UPDATE barang SET nama_barang=%s,hargabarang=%s,stok=%s,expired=%s WHERE id=%s"
                    value = (nama_barang,hargabarang,stok,expired,id)
                    cursor.execute(sql,value)
                    db.commit()
                    print('data berhasil di Update')
                updatedata()
                menu_keluar = input("Apakah Ingin Kembali Ke Menu : ").lower()
                if menu_keluar == "keluar":
                    return menu()
                else:#perintah nya enter aja keluar aplikasi + dapat daata
                    print("hasil data\nDan Anda Telah Keluar Dari aplikasi Terima kasih!!")
                    showpembelian.showpembelian()
            elif isi_menu == 11:
                showpetugas.showpetugas()
                def updatedata():
                    # tugas.showdata()
                    cursor = db.cursor()
                    id = input("pilih id Petugas : ")
                    nama_petugas = input("Masukan Nama Petugas : ")
                    email_petugas = input("Masukan Email Petugas : ")
                    nomor_petugas = input("Masukan Nomor Petugas : ")
                    sql = "UPDATE petugas SET nama_petugas=%s,email_petugas=%s,nomor_petugas=%s WHERE id=%s"
                    value = (nama_petugas,email_petugas,nomor_petugas,id)
                    cursor.execute(sql,value)
                    db.commit()
                    print('data berhasil di Update')
                updatedata()
                menu_keluar = input("Apakah Ingin Kembali Ke Menu : ").lower()
                if menu_keluar == "keluar":
                    return menu()
                else:#perintah nya enter aja keluar aplikasi + dapat daata
                    print("hasil data\nDan Anda Telah Keluar Dari aplikasi Terima kasih!!")
                    showpembelian.showpembelian()
            elif isi_menu == 12:
                showtugas.showdata()
                def deletedata():
                    cursor = db.cursor()
                    id = input("ketikan id tugas yang ingin di hapus : ")
                    sql = "DELETE FROM tugas WHERE id=%s"
                    value = (id,)
                    cursor.execute(sql,value)
                    db.commit()
                    print("data berhasil di hapus")
                deletedata()
                menu_keluar = input("Apakah Ingin Kembali Ke Menu : ").lower()
                if menu_keluar == "keluar":
                    return menu()
                else:#perintah nya enter aja keluar aplikasi + dapat daata
                    print("hasil data\nDan Anda Telah Keluar Dari aplikasi Terima kasih!!")
                    showpembelian.showpembelian()
            elif isi_menu == 13:
                showbarang.showbarang()
                def deletebarang():
                    cursor = db.cursor()
                    id = input("ketikan id user yang ingin di hapus : ")
                    sql = "DELETE FROM barang WHERE id=%s"
                    value = (id,)
                    cursor.execute(sql,value)
                    db.commit()
                    print("data berhasil di hapus")
                deletebarang()
                menu_keluar = input("Apakah Ingin Kembali Ke Menu : ").lower()
                if menu_keluar == "keluar":
                    return menu()
                else:#perintah nya enter aja keluar aplikasi + dapat daata
                    print("hasil data\nDan Anda Telah Keluar Dari aplikasi Terima kasih!!")
                    showpembelian.showpembelian()
            elif isi_menu == 14:
                showpetugas.showpetugas()
                def deletepetugas():
                    cursor = db.cursor()
                    id = input("ketikan id petugas yang ingin di hapus : ")
                    sql = "DELETE FROM petugas WHERE id=%s"
                    value = (id,)
                    cursor.execute(sql,value)
                    db.commit()
                    print("data berhasil di hapus")
                deletepetugas()
                menu_keluar = input("Apakah Ingin Kembali Ke Menu : ").lower()
                if menu_keluar == "keluar":
                    return menu()
                else:#perintah nya enter aja keluar aplikasi + dapat daata
                    print("hasil data\nDan Anda Telah Keluar Dari aplikasi Terima kasih!!")
                    showpembelian.showpembelian()
            elif isi_menu == 15:
                print("terima kasih sudah mencoba aplikasi CLI ini")
                exit()
            else:
                print("menu nggak ada ya!!\nSilahkan Isi Lagi")
                return menu()
            break
menu()