class Car:
    # fields/attribute
    marca = "Dacia"
    model = "1100"
    year = 2000
    color = "black"
    # metode
    def acelerate(self):
        print("VRUUUUUM")
    def descrie(self):
        print(f"am masina super tare {self.marca}, {self.model} din anul {self.year}")
    def stop(self):
        print("stop")

ioana = Car()
ioana.descrie()
print(ioana.color)
ioana.marca = "BMW"
ioana.color = "verde"
ioana.year = 4567
print(ioana.year)
print(ioana.color)
ioana.descrie()
ioana.marca = "Dacia"
felicia = Car()
elena = Car()
ioana.stop()
felicia.acelerate()
elena.descrie()

class Elev:
    # asa folosim parametri la clasa, ca si atribute required
    lista_note = []
    merge_la_curs=False
    # constructor
    def __init__(self, nume, prenume, cod_matricol):
        self.nume = nume
        self.prenume = prenume
        self.cod_matricol = cod_matricol

    # metode
    def descrie(self):
        print(f"Ma cheama {self.nume} {self.prenume} si am cod matricol {self.cod_matricol}")

    def adauga_nota(self, nota):
        self.lista_note.append(nota)

    def media(self):
        sum = 0
        for nota in self.lista_note:
            sum += nota
        return sum/len(self.lista_note)



elev1 = Elev("Muresan", "Ioana", 45465)
print(elev1.nume)
elev1.descrie()
print(elev1.lista_note)
elev1.adauga_nota(3)
print(elev1.lista_note)
elev1.adauga_nota(8)
print(elev1.lista_note)
print(elev1.media())
elev1.merge_la_curs = True
elev2 = Elev("Mur", "Ioana", 45465)