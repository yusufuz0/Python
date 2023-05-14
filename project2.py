# Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.
# Beden Kitle İndeksi : Kilo / Boy(m)*Boy(m)

kilo = int(input("kilonuzu giriniz: "))
boy = float(input("boyunuzu giriniz: "))


beden_kitle_indeksi = kilo/(boy*boy)

print("beden kitle indeksiniz {}".format(beden_kitle_indeksi))