# Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.

def ekok_bulma(sayi1, sayi2):

    sayi1_liste = []
    sayi2_liste = []
    ekok = 0
    b = 0

    for i in range(1,sayi2+1):
        sayi1_liste.append(i*sayi1)

    for i in range(1, sayi1 + 1):
        sayi2_liste.append(i * sayi2)

    for i in sayi1_liste:
        for x in sayi2_liste:
            if i == x:
                b = i
                ekok = i
                break

        if i == b:
            break

    return ekok


sayı1 = int(input("Sayı-1: "))
sayı2 = int(input("Sayı-2: "))

print("Ekok:", ekok_bulma(sayı1, sayı2))

