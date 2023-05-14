""" iki tane sınıf oluşturun oluşturun.
Hayvan Sınıfı ------> Bütün hayvanların ortak özelliklerinin toplandığı sınıf olacak.
Köpek Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa köpeklere ait ek özellikler ve metodlar ekleyin.
 """

import time

class hayvan():

    def __init__(self,isim,yaş,kilo,durum = "aç"):

        self.isim = isim
        self.yaş = yaş
        self.kilo = kilo
        self.durum = durum

    def besle(self):
        print("besleniyor...\n")
        time.sleep(2)
        self.durum = "tok"

    def yas_güncelle(self):
        x = input("güncel yaşını giriniz: ")
        print("yaş güncelleniyor...\n")
        time.sleep(2)
        self.yaş = x

    def kilo_güncelle(self):
        x = input("güncel kiloyu giriniz: ")
        print("kilo güncelleniyor...\n")
        time.sleep(2)
        self.yaş = x


class köpek(hayvan):

    def __init__(self,isim,yaş,kilo,cins, durum ="aç"):
        super().__init__(isim, yaş, kilo,durum)
        self.cins = cins


    def havla(self):
        print("hav hav")

    def __str__(self):
        return "köpek bilgileri:\nismi: {}\nyaşı: {}\nkilosu: {}\ndurumu: {}\ncinsi: {}".format(self.isim,self.yaş,self.kilo,self.durum,self.cins)

köpek1 = köpek("kivi",2,10,cins="golden")
print(köpek1)
köpek1.havla()
köpek1.besle()
print(köpek1)