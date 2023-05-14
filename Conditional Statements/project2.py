# Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın

s1 = int(input("sayı 1 : "))
s2 = int(input("sayı 2 : "))
s3 = int(input("sayı 3 : "))

if s1 > s2 :
    if s1> s3 :
        print(s1)
    else :
        print(s3)
elif s2 > s3  :
    print(s2)
else :
    print(s3)


# HOCANIN ÇÖZÜMÜ

""" a =  int(input("a:"))

b = int(input("b:"))

c = int(input("c:"))

if (a >= b and a >= c):
    print("En büyük sayı:",a)
elif (b >= a and b >= c):
    print("En büyük sayı:",b)
elif (c >= a and c >= b):
    print("En büyük sayı:",c)  """