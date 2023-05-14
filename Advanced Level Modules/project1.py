""" Bilgisayarınızdaki tüm mp4,txt ve pdf dosyalarını os modülüyle arayın ve bunların nerede bulunduklarını ve isimlerini ayrı ayrı "pdf_dosyalari.txt",
"mp4_dosyaları.txt","txt_dosyaları.txt" adlı dosyalara kaydedin. """

import os

pdf_yol = list()
pdf_ismi = list()

txt_yol = list()
txt_ismi = list()

mp4_yol = list()
mp4_ismi = list()


for  klasör_yolu,klasör_isimleri,dosya_isimleri in os.walk("C:\\Users\Desktop"):

    for i in dosya_isimleri:
        if i.endswith(".pdf"):
            pdf_yol.append(klasör_yolu)
            pdf_ismi.append(i)

        if i.endswith(".txt"):
            txt_yol.append(klasör_yolu)
            txt_ismi.append(i)

        if i.endswith(".mp4"):
            mp4_yol.append(klasör_yolu)
            mp4_ismi.append(i)


with open("pdf_dosyaları.txt","w",encoding="utf-8") as file:
    for i,j in zip(pdf_yol, pdf_ismi):
        file.write("bulunduğu dizin: {}\npdf ismi: {}\n\n".format(i,j))

with open("txt_dosyaları.txt","w",encoding="utf-8") as file:
    for i,j in zip(txt_yol, txt_ismi):
        file.write("bulunduğu dizin: {}\ntxt ismi: {}\n\n".format(i,j))

with open("mp4_dosyaları.txt","w",encoding="utf-8") as file:
    for i,j in zip(mp4_yol, mp4_ismi):
        file.write("bulunduğu dizin: {}\nmp4 ismi: {}\n\n".format(i,j))