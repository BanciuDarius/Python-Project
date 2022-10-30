"""6.
Avand dict
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
Vine un client cu un buget de 15000 euro
Prezentati doar masinile care se incadreaza in acest buget
Iterati prin dict.items() si accesati masina si pretul
Printati Pentru un buget de sub 15000 euro puteti alege masina x
Iterati prin lista
"""
# pret_masini = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
#
# buget = int(input(("da-mi un buget")))
# print(pret_masini.items())
# print(pret_masini.values())
# for pret in pret_masini.values():
#     if pret <=buget:
#         print(f"Pentru un buget de sub {buget} euro puteti alege masina cu pretul {pret}")
#
#
# for masina,pret in pret_masini.items():
#     if pret <= buget:
#         print(f"Pentru un buget de sub {buget} euro puteti alege masina {masina} cu pretul {pret}")


masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for masina in masini:
    print(masina)
print(masini[0])
print(masini[1])

for i in range(len(masini)):
    # print(i)
    print(masini[i])

'''Avand lista
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterati prin ea
Afisati de cate ori apare 3
(nu aveti voie sa folositi count)'''


numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

aparitii = 0
for numar in numere:
    if numar == 3:
         aparitii += 1
        # aparitii = aparitii + 1
print(aparitii)

print(numere.count(3))

'''
15.
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
Iterati prin lista 2d
Printati ‘Cifra curenta este x’
(hint: nested for - adica for in for)
'''
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
# tasta ia valori pe rand tastatura telefon[0] =[1,2,3], [4,5,6],[7,8,9], [0]
for tasta in tastatura_telefon:
    for numar in tasta:
       print(f"cifra curenta esta {numar}")

for i in range(len(tastatura_telefon)):
    print(tastatura_telefon[i])
    for j in range(len(tastatura_telefon[i])):
        print(f"cifra curenta esta {tastatura_telefon[i][j]}")


numar = int(input("vreau un numar pt piramida"))

for i in range(1,numar+1):
    print(str(i)*i)

# continue - nu mai executa urmoaToarele linii de cod din for merge direct la urmatoarea iteratie - la urmatorul element din lista , sau la urmatoarea valoare din range
# break - nu mai executa urmatoarele linii de cod din for , iese de tot din ele, nu mai este nici o iteratie, trece la urmatoare alinie de dupa for