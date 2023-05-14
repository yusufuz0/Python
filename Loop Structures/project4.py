""" Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin. Kullanıcı "q" tuşuna bastığı
 zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.

*İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın.* """

toplam = 0

while True:
    print("programdan çıkmak için q tuşuna basınız")
    sayi = input("bir sayi giriniz: ")

    if sayi == "q" :
        print("prgram sonlanıyor")
        print("toplam: ",toplam)
        break

    sayi = int(sayi)
    toplam += sayi