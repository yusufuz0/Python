# Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.

KM_başı_yakıt = float(input("araç kilometrede ne kadar yakıyor ? : "))
kilometre = int(input("kaç kilometre yol yaptınız ? : "))

ödenecek_tutar = KM_başı_yakıt*kilometre

print("ödemeniz gereken tutar {} TL dir".format(ödenecek_tutar))