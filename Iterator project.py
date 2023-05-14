""" "Kareler" isminde bir tane sınıf tanımlayın ve bu sınıfı iterable bir sınıf yapmaya çalışın. Bu sınıfın init fonksiyonu maksimum isimli bir tane parametre
alsın ve her next işleminde ekrana üzerinde bulunduğunuz sayının karesi yazdırılsın. StopIteration hatası ekrana maksimum sayıyı geçtiğiniz zaman fırlatılsın. """

class kareler():

    def __init__(self,max):
        self.max = max
        self.sayaç = 1

    def __iter__(self):
        return self


    def __next__(self):
        if self.sayaç <= self.max:
            sonuc = self.sayaç**2
            self.sayaç +=1
            return sonuc

        else:
            raise StopIteration("maksimum sayıyı geçtiniz")

kareler = kareler(5)
iterator = iter(kareler)
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())

