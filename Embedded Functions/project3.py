""" Elinizde şöyle bir liste bulunsun.

    [1,2,3,4,5,6,7,8,9,10]

Bu listenin içindeki çift sayıların toplamını ekrana yazdıran bir fonksiyon yazın.

*Not: İlk önce filter() fonksiyonu ile çift sayıları ayıklayın. Daha sonra reduce() fonksiyonunu kullanın.* """


from functools import reduce

def çifttoplam(x):
     if x %2 == 0:
         return True
     else:
         return False

def topla(x,y):

    return x+y


liste = [1,2,3,4,5,6,7,8,9,10]
dönenliste =  list(filter(çifttoplam,liste))
print(reduce(topla,dönenliste))
