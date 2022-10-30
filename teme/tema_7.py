'''ABSTRACTION
Clasa abstracta FormaGeometrica
Contine un field PI=3.14
Contine o metoda abstracta aria (optional)
Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’
INHERITANCE
Clasa Patrat - mosteneste FormaGeometrica
constructor pt latura
ENCAPSULATION
latura este proprietate privata
Implementati getter, setter, deleter pt latura
Implementati metoda ceruta de interfata (optional, doar daca ati ales sa implementati metoda abstracta aria)

Clasa Cerc - mosteneste FormaGeometrica
constructor pt raza
raza este proprietate privata
Implementati getter, setter, deleter pt raza
Implementati metoda ceruta de interfata - in calcul folositi field PI mostenit din clasa parinte (optional, doar daca ati ales sa implementati metoda abstracta aria)

POLYMORPHISM
Definiti o noua metoda descrie - printati ‘Eu nu am colturi’

'''


from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    def descrie(self):
        print("Cel mai probabil am colturi")

class Patrat(FormaGeometrica):

    def __init__(self, latura):
        self.__latura = latura

    def aria(self):
        return self.__latura* self.__latura

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print(f'Getter: latura este {self.__latura}')
        return self.__latura

    @latura.setter
    def latura(self, latura):
        print(f'Setter: Noua raza e {latura}')
        self.__latura == latura

    @latura.deleter
    def latura(self):
        print(f'Deleter: Am sters latura')
        self.__latura == None


class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Getter: Raza este {self.__raza}')
        return self.__raza

    @raza.setter
    def raza(self, raza):
        print(f'Setter: Noua raza e {raza}')
        self.__raza == raza

    @raza.deleter
    def raza(self):
        print(f'Deleter: Am sters raza')
        self.__raza == None

    def descrie(self):
        print("Eu nu am colturi")

    def aria(self):
        return self.__raza * self.__raza*self.PI

patrat = Patrat(3)
print(patrat.aria())
patrat.descrie()
# numai putem folsoi asa daca e ascuns atributul latura
print(patrat.latura)
cerc = Cerc(3)
print(cerc.aria())
print(cerc.raza)
cerc.descrie()
cerc.raza
cerc.raza = 8