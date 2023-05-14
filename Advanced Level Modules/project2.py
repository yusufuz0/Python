""" Elinizde 5 kişinin maillerinin ve isimlerinin bulunduğu bir dosya olsun. Bu dosyayı okuyarak, her bir kişiye isimleriyle beraber mail göndermeye çalışın. """


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys


with open("mailler.txt","r",encoding="utf-8") as file:
    içerikliste = file.read()
    içerikliste = içerikliste.split("\n")


for i in içerikliste:
    liste = i.split(",")


    mesaj = MIMEMultipart()  
    mesaj["From"] = "..."  
    mesaj["To"] = liste[1] 
    mesaj["Subject"] = "Smtp Mail Gönderme" 

    
    yazi = """
    
    Merhaba, Python ile mail gönderiyorum.    
    
    {}
    
    
    """.format(liste[0])

    mesaj_govdesi = MIMEText(yazi, "plain")  
    mesaj.attach(mesaj_govdesi)  

    try:
        mail = smtplib.SMTP("smtp.gmail.com", 587)  
        mail.ehlo()  
        mail.starttls()  
        mail.login("mail adresimiz","mail den aldığımız uygulama şifresi") 
        mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())  
        print("Mail başarıyla gönderildi...")
        mail.close()  

    except:
        sys.stderr.write(
            "Mail göndermesi başarısız oldu...")  
        sys.stderr.flush()