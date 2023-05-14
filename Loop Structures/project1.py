""" Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)  """

while True:
    print("çıkmak için 0 tuşuna basınız")

    sayi = int(input("bir sayı giriniz:"))

    if sayi == 0:
        break

    toplam = 0
    for i in range(1,sayi):
        if sayi % i == 0 :
            toplam += i

    if toplam == sayi:

        print("\n{} mükemmel bir sayıdır".format(sayi))

    else : print("\n{} mükemmel bir sayı değildir".format(sayi))

print("\nprogram sonlandı")
