# İleri Seviye Modüller bölümünde yazdığımız mail gönderme işlemini arayüz şeklinde yapmaya çalışın.

import sys
from PyQt5 import QtWidgets
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.setWindowTitle("Mail Gönderme")
        self.yazi = QtWidgets.QLabel("Gönderen: ...")

        self.alıcı_yazi = QtWidgets.QLabel("Alıcı: ")
        self.alıcı_input = QtWidgets.QLineEdit()

        self.konu_yazi = QtWidgets.QLabel("Konu:")
        self.konu_input = QtWidgets.QLineEdit()

        self.mesaj_alanı = QtWidgets.QTextEdit()
        self.buton = QtWidgets.QPushButton("Gönder")

        self.bilgi = QtWidgets.QLabel()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addWidget(self.alıcı_yazi)
        h_box.addWidget(self.alıcı_input)

        h_box1 = QtWidgets.QHBoxLayout()
        h_box1.addWidget(self.konu_yazi)
        h_box1.addWidget(self.konu_input)

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.yazi)
        v_box.addLayout(h_box)
        v_box.addLayout(h_box1)
        v_box.addStretch()
        v_box.addWidget(self.mesaj_alanı)
        v_box.addWidget(self.bilgi)
        v_box.addStretch()
        v_box.addWidget(self.buton)

        self.setLayout(v_box)

        self.buton.clicked.connect(self.gonder)

        self.show()


    def gonder(self):

        alıcı = self.alıcı_input.text()
        konu = self.konu_input.text()
        yazi = self.mesaj_alanı.toPlainText()

        mesaj = MIMEMultipart() 
        mesaj["From"] = "..."   
        mesaj["To"] = alıcı  
        mesaj["Subject"] = konu  

        mesaj_govdesi = MIMEText(yazi, "plain")  
        mesaj.attach(mesaj_govdesi)  

        try:
            mail = smtplib.SMTP("smtp.gmail.com",587)  
            mail.ehlo()  
            mail.starttls()  
            mail.login("mail adresimiz","mail den aldığımız uygulama şifresi")
            mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string()) 
            mail.close()  
            self.bilgi.setText("Mail Başarıyla Gönderildi...")

        except:
            self.bilgi.setText("Gönderme Başarısız...")


app = QtWidgets.QApplication(sys.argv)
pencere = pencere()
sys.exit(app.exec_())
