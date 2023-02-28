# 1 uzduotis: Sukurti funkciją, kuri priima tris parametrus:
# n - tekstas
# a - tekstas, kurio simboliai yra teigiami
# b - tekstas, kurio simboliai yra neigiami
# Teigiami simboliai yra verti 1, neigiami verti -1, o simboliai, kurių nėra nei a, nei b tekste yra vertas 0. Funkcija suskaičiuoja teksto įvertį ir jį grąžina.

def parsing_string(string):
    """Function that take string and write it as a list"""
    new_list = [x for x in string]
    return new_list


def calc_sum(n, a, b):
    """Function that calculate value by a's and b's"""
    value = 0
    # adds a's
    for letter in n:
        if letter in a:
            value += 1

        if letter in b:
            value -= 1
    return str(value)


try:
    # Defining variables & convert to list
    n = input("Please provide n:")
    list_n = parsing_string(n)
    a = input("Please provide a:")
    list_a = parsing_string(a)
    b = input("Please provide b:")
    list_b = parsing_string(b)

    # Check if there are any same values in A and B
    for char in list_b:
        if char in list_a:
            raise ValueError

    # Do main calculations
    answer = calc_sum(list_n, list_a, list_b)
    print(f'Value of text is {answer}')

except ValueError:
    print("Same values can't appear in A and B")
