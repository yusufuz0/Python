""" Süpermarket içindeki ürünler üzerinden bir tane Süpermarket Projesi geliştirmeye çalışın. """

import sqlite3
import time

bağlantı = sqlite3.connect("market.db")
cursor = bağlantı.cursor()

cursor.execute("create table if not exists ürünler(Ürün_Adı text,Ürün_Marka text,Ürün_Fiyat int,Ürün_Stok int,Ürün_STT text)")

def ürünleri_göster():
    cursor.execute("select* from ürünler")
    data = cursor.fetchall()
    for i in data:
        print(i)


def ürün_ekle(adı,marka,fiyat,stok,stt):
    cursor.execute("insert into ürünler values(?,?,?,?,?)",(adı,marka,fiyat,stok,stt))
    bağlantı.commit()

def stok_güncelle(ürün_adı,yeni_stok):
    cursor.execute("Update ürünler set Ürün_Stok = ? where Ürün_Adı = ?",(yeni_stok,ürün_adı))
    bağlantı.commit()

def fiyat_güncelle(ürün_adı,yeni_fiyat):
    cursor.execute("Update ürünler set Ürün_Fiyat = ? where Ürün_Adı = ?",(yeni_fiyat,ürün_adı))
    bağlantı.commit()

def ürün_sil(isim):
    cursor.execute("delete from ürünler where Ürün_Adı = ?",(isim,))
    bağlantı.commit()

def ürün_sorgula(isim):
    cursor.execute("select * from ürünler where Ürün_Adı = ?",(isim,))
    data = cursor.fetchall()
    for i in data:
        print(i)

def toplam_stok():
    cursor.execute("select * from ürünler")
    data = cursor.fetchall()
    toplam = 0
    for i in data:
        toplam += i[3]

    print("toplam stok : {}".format(toplam))



print("""**********************************

MARKET UYGULAMASINA HOŞGELDİNİZ

1.ürünleri göster
2.ürün ekle
3.ürün sil
4.ürün sorgula
5.stok güncelle
6.fiyat güncelle
7.toplam stok

** çıkmak için q ' ya basınız **

**********************************""")



while True:
    işlem = input("\ngerçekleştirmek istediğiniz işlemi giriniz: ")

    if işlem == "q":
        print("programdan çıkış yapılıyor...")
        time.sleep(2)
        break

    elif işlem == "1":
        ürünleri_göster()

    elif işlem == "2":
        adı = input("adı: ")
        marka = input("marka: ")
        fiyat = int(input("fiyat: "))
        stok = int(input("stok: "))
        STT = input("STT: ")
        print("yeni ürün ekleniyor...")
        time.sleep(2)
        ürün_ekle(adı,marka,fiyat,stok,STT)
        print("ürün eklendi...")

    elif işlem == "3":
        adı = input("silmek istediğiniz ürünün adını giriniz: ")
        print("ürün siliniyor...")
        time.sleep(2)
        ürün_sil(adı)
        print("ürün silindi...")

    elif işlem == "4":
        adı = input("sorgulamak istediğiniz ürünün adını giriniz: ")
        print("ürün sorgulanıyor...")
        time.sleep(2)
        ürün_sorgula(adı)

    elif işlem == "5":
        adı = input("ürünün adını giriniz: ")
        stok = int(input("yeni stok sayısını giriniz: "))
        print("stok güncelleniyor....")
        time.sleep(2)
        stok_güncelle(adı,stok)
        print("stok güncellendi...")

    elif işlem == "6":
        adı = input("ürünün adını giriniz: ")
        fiyat = int(input("ürünün yeni fiyatını giriniz: "))
        print("fiyat güncelleniyor...")
        time.sleep(2)
        fiyat_güncelle(adı,fiyat)
        print("fiyat güncellendi...")

    elif işlem == "7":
        print("stok sorgulanıyor...")
        time.sleep(2)
        toplam_stok()

    else:
        print("geçersiz işlem...")


bağlantı.close()