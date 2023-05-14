# Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın

def ebob_bul(sayi1,sayi2):
    sayi1_liste = []
    sayi2_liste = []
    aynı = []

    for i in range(1,sayi1+1):
        if sayi1 % i == 0:
            sayi1_liste.append(i)

    for i in range(1,sayi2+1):
        if sayi2 % i == 0:
            sayi2_liste.append(i)

    for i in sayi1_liste:
        for x in sayi2_liste:
            if i == x :
                aynı.append(i)


    return aynı[-1]




sayi1 = int(input("bir sayı giriniz: "))
sayi2 = int(input("bir sayı giriniz: "))
print("ebob: ",ebob_bul(sayi1,sayi2))




""" ********************************* HOCANIN ÇÖZÜMÜ *************************** """


def ebob_bulma(sayı1, sayı2):
    i = 1
    ebob = 1
    while (i <= sayı1 and i <= sayı2):

        if (not (sayı1 % i) and not (sayı2 % i)):
            ebob = i
        i += 1
    return ebob


sayı1 = int(input("Sayı-1:"))
sayı2 = int(input("Sayı-2:"))

print("Ebob:", ebob_bulma(sayı1, sayı2))