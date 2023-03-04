def firstTask():
    # Sukurti funkciją, kuri priima tris parametrus: n - tekstas, a - tekstas, kurio simboliai yra teigiami, b -
    # tekstas, kurio simboliai yra neigiami.Teigiami simboliai yra verti 1, neigiami verti - 1, o simboliai, kurių nėra
    # nei a, nei b tekste yra vertas 0. Funkcija suskaičiuoja teksto įvertį ir jį grąžina.

    def parsing_string(string):
        """Function that take string and write it as a list"""
        new_list = [x for x in string]
        return new_list

    def calc_sum(n, a, b):
        """Function that calculate value by taking "a" as PLUS and "b" as MINUS"""
        value = 0
        for letter in n:
            # Check for a's
            if letter in a:
                value += 1

            # Check for b's
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
        input()

    except ValueError:
        print("Same values can't appear in A and B")
        input()

def secondTask():
    # Sukurti funkciją, kuri priima vieną parametrą a - vienos dimensijos sąrašas. Funkcijoje atliekamas sąrašo
    # filtravimas paliekant reikšmes iš intervalo 10-100. Funkcija grąžina išfiltruotų reikšmių: vidurkį, didžiausią ir
    # mažiausią reikšmes, bei sumą. Sukurti antrą funkciją, kuri priima vieną parametrą b - sąrašą sudarytą iš sąrašų
    # ir kiekvienam sąrašo elementui iškviečia pirmą funkciją ir atspausdina gautą rezultatą.

    def filter_and_action(passed_list):
        """Function for calculating list's values in task2"""
        # Filter list for values
        filtered_values = [x for x in passed_list if x >= 10 and x <= 100]
        if not filtered_values:
            return None, None, None, None
        # Calculate rest of parameters
        avg = sum(filtered_values) / len(filtered_values)
        min_val = min(filtered_values)
        max_val = max(filtered_values)
        total = sum(filtered_values)
        return avg, min_val, max_val, total

    def list_parser(input_list):
        """Converter from few-dimensions list to one and provide calculations, check for empty"""
        for lst in input_list:
            avg, min_val, max_val, total = filter_and_action(lst)
            if avg is None:
                print("The list is empty, no output is provided")
                input()
            else:
                print("Answer:")
                print(f'({avg}, {min_val}, {max_val}, {total})')
        input()

    input_list = [
        [1, 10, 34, 110, 400, 30, 20],
        [-5, -10, 55, 120, 30],
        [2, 67, 23, 78, 200],
    ]
    print(f'List: {input_list}')
    list_parser(input_list)

def thirdTask():
    # Sukurti programą, kuri vartotojo paprašo įvesti simbolių seką - x, bei vieną skaitmenį - y. Atlikti patikrinimus,
    # jog y tikrai skaičius, jog jis yra didesnis už 0, bei x ilgis dalinasi į lygias dalis po y simbolių. Jei šios
    # sąlygos tenkinamos suskaidyti tekstą į lygias dalis po y simbolių ir atspausdinti unikalius simbolius (svarbu
    # išlaikyti simbolių eiliškumą).

    def separateText(x, y):
        sepList = []
        newStr = ""

        parts = len(x) / y
        for i in range(0, len(x)):
            if i % y == y - 1:
                newStr += x[i]
                newUniqStr = ""
                for char in newStr:
                    if char not in newUniqStr:
                        newUniqStr += char
                sepList.append(newUniqStr)
                newStr = ""

            else:
                newStr += x[i]
        return sepList

    try:
        x = input("Please enter list of chars as x: ")
        y = int(input("Please enter a single positive integer as y: "))
        if y < 0:
            print("y must be bigger than 0")
            break
        if len(x) % y != 0:
            print("Cannot divide your chars x by number you entered y!")
            break
        else:
            print(separateText(x, y))
    except ValueError:
        print("You entered a wrong value")
    break

def fourthTask():
    # Sukurti programą, kuri vartotojo paprašo įvesti simbolių seką - x, bei vieną skaitmenį - y. Atlikti patikrinimus,
    # jog y tikrai skaičius, jog jis yra didesnis už 0, bei x ilgis dalinasi į lygias dalis po y simbolių. Jei šios
    # sąlygos tenkinamos suskaidyti tekstą į lygias dalis po y simbolių ir atspausdinti unikalius simbolius (svarbu
    # išlaikyti simbolių eiliškumą).
    break


def fifthTask():
    # Sukurti funkciją, kuri atlieka teksto suspaudimą. Funkcija priima vieną parametrą x - tekstas ir grąžina tekstą
    # sudarytą iš simbolio ir jo iš eilės einančių pasikartojimų skaičiaus t.y. suspaudimas vykdomas grupuojant iš
    # eilės einančius simbolius.
    break



if __name__ == '__main__':
    while True:
        print(f'[1] First task\n[2] Second task\n[3] Third task\n[4] Fourth task\n[5] Fifth task\n\n[0] Exit')
        userInput = int(input('Enter your choice: '))
        if userInput == 1:
            firstTask()
        elif userInput == 2:
            secondTask()
        elif userInput == 3:
            thirdTask()
        elif userInput == 4:
            fourthTask()
        elif userInput == 5:
            fifthTask()
        else:
            exit(0)
2