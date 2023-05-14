""" Bir sayının çift olup olmadığını sorgulayan bir fonksiyon yazın. Bu fonksiyon, eğer sayı çift ise *return* ile bu değeri dönsün. Ancak sayı tek sayı ise
fonksiyon *raise* ile *ValueError* hatası fırlatsın. Daha sonra, içinde çift ve tek sayılar bulunduran bir liste tanımlayın ve liste üzerinde gezinerek ekrana
sadece çift sayıları bastırın. """


def çift_tek(sayi):

    if sayi == 0:
        return sayi

    elif sayi%2 == 0:
        return sayi

    else:
        raise ValueError


liste = [12,15,1,31,84,54,91,92,45,62,78,0]

for i in liste:
    try:
        print(çift_tek(i))

    except ValueError:
        pass

