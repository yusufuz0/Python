# 1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.

def pisagor_üçgeni():


    for i in range(1,101):
        for x in range(1,101):
            c= ((i**2) + (x**2))**0.5
            if (c == int(c) ):
                print(i,x,int(c))



pisagor_üçgeni()

