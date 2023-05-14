""" https://www.doviz.com/ sitesinden anlık olarak doların,euronun,altının ve borsanın değerlerini öğrenin ve bunları kullanarak bir proje geliştirmeye çalışın.

*Not: Bu projeyi, requests ve beautifulsoup kullanarak geliştirin.* """

import requests
from bs4 import BeautifulSoup
import sys
import locale
locale.setlocale(locale.LC_ALL, '')

veriler = requests.get("https://kur.doviz.com/serbest-piyasa/amerikan-dolari")
html_icerigi = veriler.content  # Web sayfamızın içeriğini alıyoruz.
soup =  BeautifulSoup(html_icerigi,"html.parser") # Web sayfamızı parçalamak için BeautifulSoup objesine atıyoruz.

name = list()
value = list()
value2 = list()


for i in soup.find_all("span",{"class":"name"}):
    name.append(i.text)
for i in soup.find_all("span",{"class":"value"}):
    value.append(i.text)

for i in value:
    if i.startswith("$"):
        a = i.lstrip("$")
        value2.append(locale.atof(a))

    else:
        value2.append(locale.atof(i))


print("********************************\n")
print(list(zip(name,value2)))
print ("""
DOLAR
EURO
GRAM ALTIN
STERLİN
BIST100
BITCOIN
GÜMÜŞ
BRENT

****************************************\n""")


doviz = input("Dovizi Giriniz: ")
miktar = input("Miktarı Giriniz: ")

try:
    a = name.index(doviz)
    x = float(miktar) * value2[a]
    print("{} TL".format(x))
except:
    sys.stderr.write("Yanlış Giriş Yaptınız...")
    sys.stderr.flush()
