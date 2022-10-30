'''
cursul asta osa fie despre variabile, assert, print, string
ffd
'''


# cum printam in consola un mesaj
print('Azi facem cursul 1!!!')
print('vfdvdvfd')
print(3434)

# variabile
# asa declaram si initializam o variabila
marca_masina = 'mazda'
model_masina = 'cx-5'
motor = 2200
este_automata = True

print(marca_masina)
print(motor)

# variabilele au nume unic, incep cu litara mica, se separa cu_, sunt case sensitive
print(marca_masina)
marca_masina = "dacia"
print(marca_masina)
Marca_masina = 'audi'
print(marca_masina)
print(Marca_masina)

# asa atribuim mai multe valori intr-o singura linie
nume, prenume, varsta = "Morar", "Ioana", 34
print(varsta)
a = b = c = 6
print(b)

marca_masina = "EFDFDdfg"
print(marca_masina)
# tipuri de date
# int - numere intregi, fara numere cu virgula
varsta = 34
print(varsta)
# asa aflu ce tip e o variabila
print(type(varsta))
# float - numere cu virgula
pret = 4.5
print(type(pret))
print(varsta+pret)

# textul - > string
print(type(marca_masina))

# bool - boolean -> True sau False
is_summer = True
print(type(is_summer))

nume, prenume, varsta = "Morar", "Ioana", 34
# type casting - > schimbam tipul variabilei -> int-> float, int -> str, sau din str sa facem float
print(nume + " " + prenume + " are varsta de " + str(varsta))
# se recomanda
print(f'Ma numesc {nume} {prenume} si am varsta de {varsta}')
print(f'Am o masina {marca_masina} ,modelul {model_masina} cu motor {motor}')

pret_masina = 1988.999
print(type(pret_masina))
pret_masina = str(pret_masina)
print(type(pret_masina))
# int(), float(), str(), bool()
pret_masina = bool(pret_masina)
print(pret_masina)

culoare = 45.5
culoare = int(culoare)
print(culoare)

# assert
mesaj_de_eroare = 'ai introdus parola gresit'
# deschid pagina
# click pe login
# type username
# type parola
# click login
# variaba;a salvez mesajul care apare pe pagina
# assert mesaj_de_eroare == "i introdus parola gresit"
# print ("ajungem la linia asta doar daca asertul e true")

# cum citim de la tastatura - functia input
ziua = input("astazi este o zi de :")
print(ziua)
latime = int(input("latimea este :"))
lungime = int(input("lungimea este"))
print(f'dreptunghiul cu latimea {latime} si lungimea {lungime} are perimetrul {latime + latime + lungime + lungime}')
# ce citim de la tastatyra e string tot timpul, daca vrem sa fie float sau int trebuie sa le transformam adica sa facem typecasting