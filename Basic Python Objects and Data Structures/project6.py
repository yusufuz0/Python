# Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.
# Hipotenüs Formülü: a^2 + b^2 = c^2

kenar1 = int(input("kenar1 giriniz: "))
kenar2 = int(input("kenar2 giriniz: "))


print("\nhipotenüs: ",(kenar1**2 + kenar2**2)**0.5)