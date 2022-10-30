'''16.
Ne imaginam o echipa de fotbal pt teren sintetic.
3 Schimbari maxime admise
Declara o Lista cu 5 jucatori
Schimbari_efectuate = va jucati voi cu valori diferite
Schimbari_max = 3

Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
Efectuam schimbarea
Stergem jucatorul scos din lista
Adaugam jucatorul intrat
Afisam a intra x, a iesit y, mai aveti z schimbari
Daca jucatorul nu e in teren:
Afisati ‘ nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
Afisati ‘mai aveti z schimbari’

Testati codul cu diferite valori

Google search hint
“how to check if item is in list python”
'''
#
schimbari_maxime = 3
jucatori = ["j1", "j2", "j3", "j4","j5"]
schimbari_efectuate = 2
jucator_in = "j8"
jucator_out = "j10"

if jucator_out in jucatori and schimbari_efectuate<3:
    print("se va efectua schimbarea")
    # ori pot sa il sterg folosind metoda remove in care trebuie sa ii dau ca si paraetru valoarea
    # stergere folosind pozitia
    # print(jucatori.index(jucator_out))
    # jucatori.pop(jucatori.index(jucator_out))
    print(jucatori)
    jucatori.remove("j4")
    print(jucatori)
    jucatori.append(jucator_in)
    print(jucatori)
    schimbari_efectuate += 1
    print(f'A iesit jucatorul {jucator_out}, a intrat jucatorul {jucator_in}, mai aveti {schimbari_maxime-schimbari_efectuate}'
          f' schimbari')
else:
    if jucator_out in jucatori:
        print("nu mai aveti schimbari")
        print(f'mai aveti {schimbari_maxime - schimbari_efectuate}')
    else:
        print(f'nu se poate efectua schimbarea deoarece jucatorul {jucator_out} nu e in teren')

lista = ["ioana", "maria", "cristina"]
lista.remove("cristina")
print(lista)
#
lista2 = ["ioana", "maria", "vasile"]
index = lista2.index("vasile")
print(f"Vasile e pe pozitia {index}")
lista2.pop(index)
print(lista2)

# cheia e unica
parole = {"chrome":"sfgd", "firefox" :"sfsgshn", "yahoo":"start", "google":"gkjh"}
pin = {"mastercard":12334, "visa":6598, "revolut":65678}
lista_produse=["aspirator", "laptop", "aragaz"]
lista_preturi=[4.55, 67.8,78.9, 456]
dict_prod = {"aspirator":4.56, "laptop":56.7,"aragaz":789}
# # asa luam lungimea
print(len(dict_prod))
# # valoarea unei key
print(dict_prod["aspirator"])
print(dict_prod.get('aspirator'))
# # adaugam elemente, update-suprascriere/modificare
dict_prod["frigider"] = 89.0
print(dict_prod)
# # key e unica
dict_prod["aspirator"] = 909
print(dict_prod)
dict_prod.update({"masa":676, "banca":890 })
print(dict_prod)
# stergere cu pop in functie de cheie
dict_prod.pop("banca")
print(dict_prod)
# # lista cu toate cheile
print(dict_prod.keys())
# # lista cu toate produsele
print(dict_prod.values())
print(dict_prod.items())
#
if "masa" in dict_prod.keys():
    print("este valoarea")

lista = ["a", "e", "i"]
if "a" in lista:
    print("e vocala")

produs = "aspirator"
if produs in dict_prod.keys():
    print("produsul e in lista de chei")
    print(dict_prod[produs])
    print(f"{produs} are pretul {dict_prod[produs]}")
    print(f"{produs} are pretul {dict_prod.get(produs)}")
else:
    print("nu e in lista")

pret = 9.99
if produs in dict_prod.values():
    print("produsul e in lista de valori")
else:
    print("nu e in lista")

# pentru conditia de unde incepe i = 0, unde se termina, si din cat in cat sa mearga


# range e un interval : de unde incepe, unde se termina si din cat in cat
# x e intre -3, 20
# x > -3  and x < 20
# -3 < x < 30
# x in range(-3, 30)
# x in range(30) exchivalent cu x in range(0,30)
# cand ne reverim la numere e i j k

for i in range(0,4):
    print(i)
    print("ana are mere")

##printeaza suma numerelor
sum = 0
for i in range(230):
    sum = sum + i*i

print(sum)
##printeaza produsul numerelor
prod = 1
for i in range(10, 230,10):
    prod = prod * i
print("am terminat")

print(prod)

masini = ["mercedes", "volvo", "dacia", "trabant", "aro"]
len = len(masini)
for i in range(len):
    print(masini[i])
    if masini[i] == "volvo":
        masini[i] = "cielo"
    if masini[i].islower():
        masini[i] = masini[i].upper()
print(masini)

# for each
for masina in masini:
    print(masina)

culori=["alb", "verde", "roz"]
for culoare in culori:
    print(culoare)
    if culoare == "verde":
        culori.remove(culoare)
print(culori)

parole = {"chrome":"sfgd", "firefox" :"sfsgshn", "yahoo":"start", "google":"gkjh"}
for key, value  in parole.items():
    print(f"situl {key} are parola {value}")

vocale = ["a", "e", "i"]
for vocala in vocale:
    print(vocala)

# break - sare peste pasi urmatri , iese din cod

masini = ["mercedes", "volvo", "dacia", "trabant", "aro"]
for masina in masini:
    print(masina)
    if masina == "volvo":
        print("cea mai tare din parcare")
        break

# continue - sare peste peste pasi si merge la urmatoarea teratie

for masina in masini:
    if masina == "volvo":
        print("cea mai tare din parcare")
        continue
    print(masina + masina)