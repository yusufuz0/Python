""" Elinizde uzunca bir string olsun  "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb" Bu string içindeki harflerin frekansını (bir harfin kaç defa geçtiği)
 bulmaya çalışın. """


x = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"

liste1 = list()
liste2 = list()

for i in x:
   a = x.count(i)
   liste1.append(a)
   liste2.append(i)

liste3 = list(zip(liste1,liste2))

küme= set(liste3)
for i,j in küme:
   print("{} : {}".format(j,i))

"""******************* HOCANIN ÇÖZÜMÜ **************************
s = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
frekans = dict()

for karakter in s:
   if (karakter in frekans):
      frekans[karakter] += 1
   else:
      frekans[karakter] = 1
for i, j in frekans.items():
   print(i, ":", j) """