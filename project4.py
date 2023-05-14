# Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.

ad = input("adınız: ")
soyad = input("soyadınız: ")
numara = int(input("numaranız: "))

print("\nBilgiler...\n")

print("{} \n{} \n{}".format(ad,soyad,numara))