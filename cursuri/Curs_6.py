# # Bubble sort in Python
# data = [-2, 45, 0, 11, -9]
# def bubbleSort(lista):
#     # loop to access each array element
#     for i in range(len(lista)):
#         # loop to compare array elements
#         for j in range(0, len(lista) - i - 1):
#
#             # compare two adjacent elements
#             # change > to < to sort in descending order
#             if lista[j] > lista[j + 1]:
#                 # swapping elements if elements
#                 # are not in the intended order
#                 temp = lista[j]
#                 lista[j] = lista[j + 1]
#                 lista[j + 1] = temp
#
#
#
# bubbleSort(data)
#
# print('Sorted Array in Ascending Order:')
# print(data)
#
# '''7. Functie fara return, primeste un string si printeaza pe ecran:
# Nr de caractere lower case este x
# Nr de caractere upper case exte y
# '''
# text = "fdfdfgdg"
# def number_lower_upper(text):
#     lower = 0
#     upper = 0
#     for litera in text:
#         if litera.isupper():
#             upper += 1
#         else:
#             if litera.islower():
#                 lower += 1
#     print(f'{text} are {lower} atatea caractere mici si {upper} atatea caractere mari')
#
# def number_lower_upper2(text):
#     lower = 0
#     upper = 0
#     for i in range(len(text)):
#         if text[i].isupper():
#             upper += 1
#         else:
#             if text[i].islower():
#                 lower += 1
#     print(f'{text} are {lower} atatea caractere mici si {upper} atatea caractere mari')
#
# number_lower_upper("FGHJKJ")
# number_lower_upper("fdfgfdg")
# number_lower_upper("SDFyyy")
# number_lower_upper2("As234")
# number_lower_upper2("Ce mai faci?")


def text():
    # printeaza ceva ori returneaza
    print(" fara return")

text()

def get_name():
    # printeaza ceva ori returneaza
    return  5

def get_aria():
    return 10

def is_prim():
    pass

def is_submit_button_displayed():
    return True

print(text())

varsta = text()
print(varsta)

# care returneaza TRue sau folse incep cu is_
#care ne dau un text sau o valoare incep cu get_

def este_par(numar):
    if numar%2 == 0:
        return True
    else:
        return False

def este_par2(numar):
    return numar%2 == 0


print(este_par(3))
print(este_par(310))
print(este_par2(310))

def number_lower_upper2(text):
    lower = 0
    upper = 0
    for i in range(len(text)):
        if text[i].isupper():
            upper += 1
        else:
            if text[i].islower():
                lower += 1
    print(f'{text} are {lower} atatea caractere mici si {upper} atatea caractere mari')
    if lower == len(text) or upper ==len(text):
        return True
    else:
        return False
toate_lietere_de_un_fel = number_lower_upper2("Ad")
print(toate_lietere_de_un_fel)
toate_lietere_de_un_fel = number_lower_upper2("HFJGKJLKLK")
print(toate_lietere_de_un_fel)

def login(user, password ="123"):
    print(f"Ma loghez cu user {user} parola {password}")


login("ioana", "123")
login("vasile", "@#@$$#%")
login("admin")


def perimetru(latime, lungime):
    return 2*latime+2*lungime
