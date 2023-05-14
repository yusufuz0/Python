"""   bir tane Şarkı projesi geliştirmeye çalışın.
 Örnek özellikler;

1. Şarkı İsmi
2. Sanatçı
3. Albüm
4. Prodüksiyon Şirket
5. Şarkı Süresi

 Örnek Metodlar;

1. Veritabanındaki Toplam Şarkı Süresini Hesaplayan Metod
2. Şarkı Ekle
3. Şarkı Sil """


import sqlite3
import time

class playlist():

    def __init__(self):

        self.bağlantı = sqlite3.connect("playlist.db")
        self.cursor = self.bağlantı.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS şarkılar (isim TEXT, sanatçı TEXT, süre INT)")
        self.bağlantı.commit()

    def şarkıları_göster(self):
        self.cursor.execute("select * from şarkılar")
        data = self.cursor.fetchall()
        for i in data:
            print(i)

    def şarkı_sorgula(self,isim):
        self.cursor.execute("select * from şarkılar where isim = ?",(isim,))
        data = self.cursor.fetchall()
        if len(data) == 0 :
          print("böyle bir şarkı bulunmuyor...")
        else:
            print(data)


    def toplam_süre(self):
        self.cursor.execute("select* from şarkılar")
        data = self.cursor.fetchall()
        toplam = 0
        for i in data:
            toplam +=i[2]
        print(toplam)


    def şarkı_ekle(self,isim,sanatçı,süre):

        self.cursor.execute("insert into şarkılar values(?,?,?)",(isim,sanatçı,süre))
        self.bağlantı.commit()

    def şarkı_sil(self,isim):
        self.cursor.execute("select * from şarkılar where isim = ?",(isim,))
        data =  self.cursor.fetchall()
        if len(data) == 0 :
            print("zoten böyle bir şarkı bulunmuyor...")
        self.cursor.execute("delete from şarkılar where isim = ?",(isim,))
        self.bağlantı.commit()



print("""*********************************

Playlist Uygulamasına Hoşgeldiniz

1.şarkıları göster
2.şarkı ekle
3.şarkı sorgula
4.şarkı sil
5.playlistin toplam süresi

çıkmak için q' ya basınız

*********************************""")

p1 = playlist()

while True:

    işlem =  input("\nişlemi giriniz: ")

    if işlem == "q":
        print("program sonlandırılıyor...")
        break

    elif işlem == "1":
        p1.şarkıları_göster()


    elif işlem == "2":
        isim = input("isim: ")
        sanatçı = input("sanatçı: ")
        süre = int(input("süre: "))
        print("şarkı ekleniyor...")
        time.sleep(2)
        p1.şarkı_ekle(isim,sanatçı,süre)


    elif işlem == "3":
        isim = input("şarkının ismini giriniz: ")
        print("şarkı sorgulanıyor...")
        time.sleep(2)
        p1.şarkı_sorgula(isim)

    elif işlem == "4":
        isim = input("silmek istediğiniz şarkı ismi: ")
        print("şarkı siliniyor...")
        time.sleep(2)
        p1.şarkı_sil(isim)

    elif işlem == "5":
        p1.toplam_süre()














