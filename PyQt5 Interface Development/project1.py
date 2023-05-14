# İleri Seviye Modüller bölümünde yazdığımız döviz programı arayüz şeklinde yapmaya çalışın

import sys
from PyQt5.QtWidgets import QWidget,QApplication,QRadioButton,QLabel,QPushButton,QVBoxLayout,QLineEdit,QTextEdit,QHBoxLayout
import requests
from bs4 import BeautifulSoup
import locale

class pencere(QWidget):

    def __init__(self):
        super().__init__()
        self.verileriçek()
        self.init_ui()


    def verileriçek(self):
        locale.setlocale(locale.LC_ALL, '')
        veriler = requests.get("https://kur.doviz.com/serbest-piyasa/amerikan-dolari")
        html_icerigi = veriler.content  # Web sayfamızın içeriğini alıyoruz.
        soup = BeautifulSoup(html_icerigi,"html.parser")  # Web sayfamızı parçalamak için BeautifulSoup objesine atıyoruz.

        self.value = list()
        self.value2 = list()

        for i in soup.find_all("span", {"class": "value"}):
            self.value.append(i.text)

        for i in self.value:
            if i.startswith("$"):
                a = i.lstrip("$")
                self.value2.append(locale.atof(a))

            else:
                self.value2.append(locale.atof(i))


    def init_ui(self):

        self.setWindowTitle("Döviz Uygulaması")

        self.yazi = QLabel("Miktar: ")
        self.input = QLineEdit()

        self.altın = QRadioButton("Gram Altın")
        self.dolar = QRadioButton("Dolar")
        self.euro= QRadioButton("Euro")
        self.sterlin = QRadioButton("Sterlin")
        self.gümüş = QRadioButton("Gümüş")

        self.sonuc = QTextEdit("")
        self.buton = QPushButton("ÇEVİR")

        h_box = QHBoxLayout()
        h1_box = QHBoxLayout()
        v_box = QVBoxLayout()

        v_box.addLayout(h_box)
        v_box.addLayout(h1_box)
        v_box.addStretch()
        v_box.addWidget(self.sonuc)
        v_box.addWidget(self.buton)

        h1_box.addWidget(self.altın)
        h1_box.addWidget(self.dolar)
        h1_box.addWidget(self.euro)
        h1_box.addWidget(self.sterlin)
        h1_box.addWidget(self.gümüş)


        h_box.addWidget(self.yazi)
        h_box.addWidget(self.input)
        self.setLayout(v_box)

        self.buton.clicked.connect(lambda : self.click(self.altın.isChecked(),self.dolar.isChecked(),self.euro.isChecked(),self.sterlin.isChecked(),self.gümüş.isChecked()))

        self.show()

    def click(self,altın,dolar,euro,sterlin,gümüş):
        try:
            if altın:
                x = float(self.input.text())
                a = str(round(x * self.value2[0],2)) + " TL"
                self.sonuc.setText(a)

            if dolar:
                x = float(self.input.text())
                a = str(round(x * self.value2[1],2)) + " TL"
                self.sonuc.setText(a)

            if euro:
                 x = float(self.input.text())
                 a = str( round(x * self.value2[2],2)) + " TL"
                 self.sonuc.setText(a)

            if sterlin:
                 x = float(self.input.text())
                 a = str(round(x * self.value2[3],2)) + " TL"
                 self.sonuc.setText(a)

            if gümüş:
                x = float(self.input.text())
                a = str(round(x * self.value2[6],2)) + " TL"
                self.sonuc.setText(a)
        except:
            self.sonuc.setText("Yanlış Giriş Yaptınız...")


app = QApplication(sys.argv)
pencere = pencere()
sys.exit(app.exec_())