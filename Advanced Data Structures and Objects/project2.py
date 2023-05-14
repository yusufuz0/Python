""" Elinizde 5 kişinin maillerinin ve isimlerinin bulunduğu bir dosya olsun. Bu dosyayı okuyarak, her bir kişiye isimleriyle beraber mail göndermeye çalışın. """
# wmgegfjmclrqtqjd

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys


with open("mailler.txt","r",encoding="utf-8") as file:
    içerikliste = file.read()
    içerikliste = içerikliste.split("\n")


for i in içerikliste:
    liste = i.split(",")


    mesaj = MIMEMultipart()  # Mail yapımızı oluşturuyoruz.
    mesaj["From"] = "uzysf2001@gmail.com"  # Kimden Göndereceğimiz
    mesaj["To"] = liste[1] # Kime Göndereceğimiz
    mesaj["Subject"] = "Smtp Mail Gönderme"  # Mailimizin Konusu

    # Mailimizin İçeriği
    yazi = """
    
    Merhaba, Python ile mail gönderiyorum.    
    
    {}
    
    
    """.format(liste[0])

    mesaj_govdesi = MIMEText(yazi, "plain")  # Mailimizin gövdesini bu sınıftan oluşturuyoruz.
    mesaj.attach(mesaj_govdesi)  # Mailimizin gövdesini mail yapımıza ekliyoruz.

    try:
        mail = smtplib.SMTP("smtp.gmail.com", 587)  # SMTP objemizi oluşturuyoruz ve gmail smtp server'ına bağlanıyoruz.
        mail.ehlo()  # SMTP serverına kendimizi tanıtıyoruz.
        mail.starttls()  # Adresimizin ve Parolamızın şifrelenmesi için gerekli
        mail.login("uzysf2001@gmail.com","wmgegfjmclrqtqjd")  # SMTP server'ına giriş yapıyoruz. Kendi mail adresimizi ve parolamızı yapıyoruz.
        mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())  # Mailimizi gönderiyoruz.
        print("Mail başarıyla gönderildi...")
        mail.close()  # Smtp serverımızın bağlantısını koparıyoz.

    except:
        sys.stderr.write(
            "Mail göndermesi başarısız oldu...")  # Herhangi bir bağlanma sorunu veya mail gönderme sorunu olursa
        sys.stderr.flush()