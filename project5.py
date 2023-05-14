# Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.

sayi1 = int(input("sayı1 giriniz: "))
sayi2 = int(input("sayı2 giriniz: "))

print("sayi1: {} \nsayi2: {}".format(sayi1,sayi2))

sayi1,sayi2 = sayi2,sayi1

print("\nsayılar değiştirildi.... \n")

print("sayi1: {} \nsayi2: {}".format(sayi1,sayi2))