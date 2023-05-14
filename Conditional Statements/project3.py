""" Kullanıcının girdiği vize1,vize2,final notlarına göre harf notunu hesaplayın.
    Vize1 toplam notun %30'una etki edecek.
    Vize2 toplam notun %30'una etki edecek.
    Final toplam notun %40'ına etki edecek.
    Toplam Not >=  90 -----> AA
    Toplam Not >=  85 -----> BA
    Toplam Not >=  80 -----> BB
    Toplam Not >=  75 -----> CB
    Toplam Not >=  70 -----> CC
    Toplam Not >=  65 -----> DC
    Toplam Not >=  60 -----> DD
    Toplam Not >=  55 -----> FD
    Toplam Not <  55 -----> FF  """


vize1 = int(input("vize1 notunu giriniz: "))
vize2 = int(input("vize2 notunu giriniz: "))
final = int(input("final notunu giriniz: "))

ort = (vize1*0.3) + (vize2*0.3) + (final*0.4)
print("dersin ortalama notu: ", ort)

if ort >= 90 :
    print("AA")
elif ort >= 85 :
    print("BA")
elif ort >= 80 :
    print("BB")
elif ort >= 75 :
    print("CB")
elif ort >= 70 :
    print("CC")
elif ort >= 65 :
    print("DC")
elif ort >= 60 :
    print("DD")
elif ort >= 55 :
    print("FD")
else :
    print("FF")



