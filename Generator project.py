# 1'den 1000'e kadar olan sayılardan asal sayıları üreten generator bir fonksiyon yazın.

def asal_generator():
    for i in range(2,1001):
        sayı = 0
        for x in range(2,i):
            if i % x == 0:
                sayı += 1
                break

        if sayı == 0:
            yield i




for i in asal_generator():
    print(i)
