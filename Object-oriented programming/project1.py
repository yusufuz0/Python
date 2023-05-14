""" Bir tane "Bilgisayar" sınıfı oluşturarak bu sınıfa metodlar ve özellikler ekleyin ve bu class'ı kullanmaya çalışın. """

import random
import time

class bilgisayar:

     def __init__(self,ram = 4,ssd = 220, kullanıcı_listesi= ["yusuf"], kullanıcı="yusuf",bilgisayar_durumu="kapalı"):

         self.ram = ram
         self.ssd =ssd
         self.kullanıcı_listesi = kullanıcı_listesi
         self.kullanıcı = kullanıcı
         self.bilgisayar_durumu = bilgisayar_durumu

     def bilgisayarı_aç(self):
         if self.bilgisayar_durumu == "açık":
             print("bilgisayar zaten açık...")

         else:
             print("bilgisayar açılıyor...")
             time.sleep(2)
             self.bilgisayar_durumu == "açık"


     def bilgisayar_kapat(self):
         if self.bilgisayar_durumu == "kapalı":
             print("bilgisayar zaten kapalı...")

         else:
             print("bilgisayar kapatılıyor...")
             time.sleep(2)
             self.bilgisayar_durumu == "kapalı"



     def ram_değis(self):

         print("ram i artırmak için: +\nram i azaltmak için: -\ndeğiştirmek istemiyorsanız: iptal")
         işlem = input("işlem: ")

         if işlem == "+":
             x = input("artırmak istediğiniz ram seviyesini giriniz: ")
             print("ram artırılıyor...")
             time.sleep(1)
             self.ram = x

         elif işlem == "-":
            x = input("azaltmak istediğiniz ram seviyesini giriniz: ")
            print("ram azaltılıyor...")
            time.sleep(1)
            self.ram = x

         elif işlem == "iptal":
            print("çıkış yapılıyor....")
            time.sleep(1)



     def ssd_değiş(self):


        print("ssd i artırmak için: +\nssd i azaltmak için: -\ndeğiştirmek istemiyorsanız: iptal")
        işlem = input("işlem: ")

        if işlem == "+":
             x = input("artırmak istediğiniz ssd seviyesini giriniz: ")
             print("ssd artırılıyor...")
             time.sleep(1)
             self.ssd = x

        elif işlem == "-":
             x = input("azaltmak istediğiniz ssd seviyesini giriniz: ")
             print("ssd azaltılıyor...")
             time.sleep(1)
             self.ssd = x


        elif işlem == "iptal":
             print("çıkış yapılıyor....")
             time.sleep(1)


     def kullanıcı_ekle(self):

         x =  input("eklemek istediğiniz kullanıcıyı giriniz: ")
         print("kullanıcı ekleniyor...")
         time.sleep(1)
         self.kullanıcı_listesi.append(x)



     def kullanıcı_değiş(self):
         x = random.randint(0,len(self.kullanıcı_listesi)-1)
         print("kullanıcı değiştiriliyor...")
         time.sleep(1)
         self.kullanıcı = self.kullanıcı_listesi[x]



     def __str__(self):
         return "Bilgisayar: {}\nram: {}\nssd: {}\nkullanıcılar: {}\nşu anki kullancı: {}".format(self.bilgisayar_durumu,self.ram,self.ssd,self.kullanıcı_listesi,self.kullanıcı)

bilgisayar1 = bilgisayar()


print("""
**************** BİLGİSAYAR UYGULAMASI ************* 
     
    1.BİLGİSAYAR BİLGİLERİ
    
    2.BİLGİSAYARI AÇ
    
    3.BİLGİSAYARI KAPAT
    
    4.RAM DEĞİŞ

    5.SSD DEĞİŞ

    6.KULLANICI EKLE

    7.KULLKANICI DEĞİŞ
    
    ÇIKMAK İÇİN Q YABASINIZ
    
    """)

while True:

    işlem = input("\nişlemi giriniz: ")

    if işlem == "1":
        print(bilgisayar1)
    elif işlem == "4":
        bilgisayar1.ram_değis()
    elif işlem == "5":
        bilgisayar1.ssd_değiş()
    elif işlem == "6":
        bilgisayar1.kullanıcı_ekle()
    elif işlem == "7":
        bilgisayar1.kullanıcı_değiş()
    elif işlem == "2":
        bilgisayar1.bilgisayarı_aç()
    elif işlem == "3":
        bilgisayar1.bilgisayar_kapat()
    elif işlem == "q":
        print("çıkış yapılıyor...")
        break
    else:
        print("geçersiz giriş.....")




























