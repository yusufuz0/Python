""" Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.
Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.
Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın.
Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.
Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz. Kullanımı şu şekildedir ;
abs(-4)
4
abs(5)
5  """

print("üçgenin tipini bulmak isterseniz :1 \ndörtgenin tipini bulmak isterseniz : 2")
işlem = input("1 or 2 : ")

if işlem == "1" :
    k1 = int(input("kenar1: "))
    k2 = int(input("kenar2: "))
    k3 = int(input("kenar3: "))

    if  ( abs(k1+k2) > k3 and abs(k1+k3) > k2 and abs(k2+k3) > k1) :

        if k1 == k2 == k3 :
            print("eşkenar üçgen")
        elif (k1 == k2 or k1 == k3)  and (k2 == k3) :
            print("ikizkenar üçgen")
        else:
            print("çeşitkenar üçgen")

    else :
        print("üçgen belirtmiyor")



elif işlem == "2" :
    k1 = int(input("kenar1: "))
    k2 = int(input("kenar2: "))
    k3 = int(input("kenar3: "))
    k4 = int(input("kenar4: "))

    if k1 == k2 == k3 == k4 :
        print("kare")
    elif ( k1 == k2 and k3 == k4 ) or (k1 == k3 and k2 == k4) or (k1 == k4 and k2 == k3 ) :
        print("diktörtgen")
    elif k1 <= 0 or k2 <= 0 or  k3 <= 0 or  k4 <= 0 :
        print("dörtgen belirtmiyor")
    else :
        print("sıradan dörtgen")

















