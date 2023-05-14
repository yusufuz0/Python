# BASİT HESAP MAKİNESİ

print("TOPLAMA : 1 \nÇIKARMA : 2 \nÇARPMA : 3 \nBÖLME : 4\n\n")

a = int(input("birinci sayıyı giriniz: "))
b = int(input("ikinci sayıyı giriniz: "))

işlem = int(input("işlem: "))

if işlem == 1 :
    print("sonuç: ",a+b)

elif işlem == 2 :
    print("sonuç: ", a - b)

elif işlem == 3 :
    print("sonuç: ", a*b )

elif işlem == 4 :
    print("sonuç: ", a / b)

else :
    print("hatalı giriş yaptınız")

