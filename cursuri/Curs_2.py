# '''
# string, operatori, if
# '''
#
#
text = 'alabala portocala*'

# fiecare caracter are un index asociat
# numaratoarea incepe de la 0
# lungimea - len
print(len(text))
# metodele cu is in fata returneaza true sau False si se pot folosi la assert
print(text.isnumeric())
assert  text.islower()
# printa fiecare caracter in functie de index
print(text[0])
print(text[3])
# print ultiml caracter
print(text[-1])
# - nu se recomanda
print(text[17])
# print(text[18])
print(text[len(text)-1])
# de unde incepem, pana unde(-1) - interval deschis
print(text[3:7])
print(text[0:7])
print(text[:7])
# printeaza de la poz 3 pana la final
print(text[3:])
print(text[::2])
print(text[1::2])
print(text[1::5])
# textul invers
print(text[::-1])
# slicing
print(text.capitalize())
print(text.upper())

numar = int(input("vreau un numar"))
print(text[numar])
print(text.replace("bala", "apa"))
# de unde incepem, pana unde-1, din cat in cat
print(text[1:5:2])
# primul element, pt ultimul element si daca mer din unu in unu nu e neaparat sa pun ceva  , pt ca dac anu pun nimic mi le ia by default
#  daca nu pun nimic pe pozitie 1 considera poz 0
print(text[:5:2])
#  daca nu pun nimic pe  pozitie 2 considera se considera ultima pozitie
# adica o sa imi afiseze pana la ultima pozitie inclusiv
print(text[::2])
#  daca nu pun nimic pe  pozitie 3 considera se considera ca merg din 1 in 1, adica efectiv tot stringul
print(text[::])

# operatori de atribuire, aritmetici, de comparare, logici

# operatori de atribuire: = , +=, -=, /=, *=
maxim = 8
# incrementare
maxim += 1
maxim = maxim +1
maxim += 10
print(maxim)
maxim -= 5
maxim = maxim -5
maxim *=2
maxim = maxim *2
maxim /=3
maxim = maxim//3
print(maxim)
# operatori aritmetici
# +, -, % restul impartirii, // catul, / impartire, * inmultire, ** - putere
print(3**2)
print("tatatatatata")
print("ta"*6)
numar1 = int(input("vreau un numar"))
numar2 = int(input("vreau al doilea numar"))
print(f'Produsul numerelor este {numar1*numar2}')

# operatori de comparare
# ==, >=, >, <, <=,!=- not equal

assert 5!=6

#operatori logici
#  and care returneaza True daca amandoua conditiile sunt adevarate
# se foloseste la intervale, sau cand doua conditii trebuie sa fie indeplinite simultan
numar = 11
# assert numar>=2 and numar<=10
# assert varsta >= 14 and un parinte e cu tine and parintele e proprietar

# or - sau minim una din conditii trebuie sa fie adevarata
assert numar>=2 or numar<=10
# not

assert 5!=6
assert not 5==5

# if - flow control, controlam pe unde mereg codul , sau ce se intampla, - daca

parola2 = "start123"
user = input("introdu userul")
parola = input("introdu parola")

# ce e in interiorul if-ul se ruleaza doardaca conditia e adevarata
if parola == parola2:
    print("te-ai logat cu succes")
else:
    print("parola nu e corecta")

if user[0] == 'a':
    print("userul e corect")

numar = 10
numar2 = int(input("vreau un numar"))
if numar2 > numar:
    print(f'{numar2} este maximul')
else:
    print(f'{numar} este maximul')
# daca o conditie e adevarata sau falsa - in functie de asta facem sau executam alte linii de cod

if numar2 > 5 and numar2 < 30:
    print("numarul e in interval")

if 5 < numar2 < 30:
    print("numarul e in interval")
  # a+b * c (a+b)*c
# if  user == "cont norma " and parola= "FDDG" or admin fghg
# if  (varsta > 18 and ai pasaport) or (varsta <18 and (e mama or e tata)) or ()
# # if, if else, elif

nota = 7
if nota>9 :
    print("a luat premiul intai")
elif  nota>8:
    print("a luat premiul doi")
else:
    print("retsul au luat locul 3")

if  suma== 40:
    print("ai abonamnet de 1 giga")
elif suma == 30:
    print ("ai abonament de 500 mb")
elif suma == 20:
    print ("ai cel mai ieftin abonamant")
else:
    print("ai prea putini bani si nu ai net")

luna = input ("da-mi un nume de luna")
an = int ("da-mi anul curent")
if luna == "decembrie " or luna ==" martie" or luna == "iunie":
    print("au 30 de zile")
elif luna == "ianuarie" or luna == "iulie":
    print("are 31 zile")
else:
    # verific daca e multiplu de 4 atunci restul impartirii e 0
    if an%4==0:
        print ("are 29 zile")
    else:
        print("are 28 zile")


# nu avem cod pe partea de true
if  not(23 >10):
    print("EGDFGDFh")
print(max(45,67,89,78))
from datetime import date

today = date.today()
print("Today's date:", today)