""" Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.

 Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez """


boy = float(input("boyunuz: "))
kilo = float(input("kilonuz: "))

bki = kilo / (boy*boy)
print(" beden kitle indeksi :",bki)

if bki < 18.5 :
    print("zayıf")

elif 18.5 <= bki <= 25  :
    print("normal")

elif  25 < bki <= 30:
    print("kilolu")

else: 
    print("obez")

