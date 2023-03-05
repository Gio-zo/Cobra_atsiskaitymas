# Klausimas: Ar kinamieji turi buti pavadinti kaip pateikta uzduotyje?! a,b,x,y ir t.t.???
def firstTask():
    # Sukurti funkciją, kuri priima tris parametrus: n - tekstas, a - tekstas, kurio simboliai yra teigiami, b -
    # tekstas, kurio simboliai yra neigiami.Teigiami simboliai yra verti 1, neigiami verti - 1, o simboliai, kurių nėra
    # nei a, nei b tekste yra vertas 0. Funkcija suskaičiuoja teksto įvertį ir jį grąžina.

    def parsing_string(user_string):
        # Function that take string and write it as a list
        new_list = []
        for x in user_string:
            new_list.append(x)
        return new_list

    def calc_sum(n, a, b):
        # Function that calculate value by taking "a" as PLUS and "b" as MINUS
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
        # Function for calculating list's values
        filtered_values = []  # This is where new list of filtered values is saved
        try:
            for x in passed_list:
                if int(x) >= 10 and int(x) <= 100:
                    filtered_values.append(int(x))  # Convert x (passed list value) to int before appending
        except ValueError:
            print("Something wrong with values")
            return None, None, None, None  # Return early if ValueError occurs
        if not filtered_values:
            return None, None, None, None
        # Calculate task of parameters
        avg = sum(filtered_values) / len(filtered_values)
        min_val = min(filtered_values)
        max_val = max(filtered_values)
        total = sum(filtered_values)
        return avg, min_val, max_val, total

    def list_parser(input_list):
        # Converter from few-dimensions list to one and do calculations, check for empty
        for b in input_list:  # Do all necessary calculations on each list dimension
            avg, min_val, max_val, total = filter_and_action(b)  # call function and get answers
            if avg is None:
                print("The list is empty, no output is provided")
            else:
                print("Answer:")
                print(f'({avg}, {min_val}, {max_val}, {total})')

    user_list = []  # this list stores final user input list
    while True:
        a = input("Please provide comma separated integer list: ")
        newlist = a.split(',')
        user_list.append(newlist)
        choice = input("Do you want to continue filling the list? [y/n]")
        if choice.lower() == "y":  # Used lower() to handle uppercase input
            continue  # Get user input while answer is y, get back to while True
        elif choice.lower() == "n":  # activate if user finished with inputting list (choose n)
            print(f'List: {user_list}')
            list_parser(user_list)  # Call functions to execute all necessary calculations
            return
        else:
            print("Wrong input, exiting task 2")
            return


def thirdTask():
    # Sukurti programą, kuri vartotojo paprašo įvesti simbolių seką - x, bei vieną skaitmenį - y. Atlikti patikrinimus,
    # jog y tikrai skaičius, jog jis yra didesnis už 0, bei x ilgis dalinasi į lygias dalis po y simbolių. Jei šios
    # sąlygos tenkinamos suskaidyti tekstą į lygias dalis po y simbolių ir atspausdinti unikalius simbolius (svarbu
    # išlaikyti simbolių eiliškumą).

    def separateText(x, y):
        sepList = []  # empty list for result
        newStr = ""  # temp empty string for appending values

        for i in range(0, len(x)):
            print(i % y)
            if i % y == y - 1:  # checking if i value is last that we need to get
                newStr += x[i]
                newUniqStr = ""  # new string for unique values
                for char in newStr:
                    if char not in newUniqStr:
                        newUniqStr += char  # if value is unique - append
                sepList.append(newUniqStr)
                newStr = ""  # clear temp string

            else:
                newStr += x[i]  # if not last value
        return sepList

    try:
        x = input("Please enter list of chars as x: ")
        y = int(input("Please enter a single positive integer as y: "))
        if y < 0:
            print("y must be bigger than 0")
            return
        if len(x) % y != 0:
            print("Cannot divide your chars x by number you entered y!")
            return
        else:
            print(separateText(x, y))
    except ValueError:
        print("You entered a wrong value")
    return


def fourthTask():
    # Sukurti dekoratorių antros užduoties funkcijai, kuri grąžina vidurkį, didžiausią ir mažiausią reikšmes,
    # bei sumą. Dekoratorius priima vieną parametrą x - skaičių. Atimti parametrą x iš kiekvienos dekoruojamos
    # funkcijos grąžinamos reikšmės.

    def remove_number_decorator(func):
        def wrapper(*args):
            avg, min_val, max_val, total = func(*args)  # Call the original function
            if avg is not None:  # check if avg is not empty
                # Subtract user imputed num from results
                avg -= x
                min_val -= x
                max_val -= x
                total -= x
            # Return the updated average and other values
            return avg, min_val, max_val, total

        return wrapper

    @remove_number_decorator
    def filter_and_action(passed_list):
        # Function for calculating list's values
        filtered_values = []  # This is where new list of filtered values is saved
        try:
            for x in passed_list:
                if int(x) >= 10 and int(x) <= 100:
                    filtered_values.append(int(x))  # Convert x (passed list value) to int before appending
        except ValueError:
            print("Something wrong with values")
            return None, None, None, None  # Return early if ValueError occurs
        if not filtered_values:
            return None, None, None, None
        # Calculate task of parameters
        avg = sum(filtered_values) / len(filtered_values)
        min_val = min(filtered_values)
        max_val = max(filtered_values)
        total = sum(filtered_values)
        return avg, min_val, max_val, total

    def list_parser(input_list):
        # Converter from few-dimensions list to one and do calculations, check for empty
        for b in input_list:  # Do all necessary calculations on each list dimension
            avg, min_val, max_val, total = filter_and_action(b)  # call function and get answers
            if avg is None:
                print("The list is empty, no output is provided")
            else:
                print("Answer:")
                print(f'({avg}, {min_val}, {max_val}, {total})')

    user_list = []  # this list stores final user input list
    while True:
        user_input = input("Please provide comma separated integer list: ")
        newlist = user_input.split(',')
        user_list.append(newlist)
        choice = input("Do you want to continue filling the list? [y/n]")
        if choice.lower() == "y":  # Used lower() to handle uppercase input
            continue  # Get user input while answer is y, get back to while True
        elif choice.lower() == "n":  # activate if user finished with inputting list (choose n)
            x = int(input("Enter a number to remove: "))  # get number that user what to subtract from results
            print(f'List: {user_list}')
            list_parser(user_list)  # Call functions to execute all necessary calculations
            return
        else:
            print("Wrong input, exiting task 2")
            return


def fifthTask():
    # Sukurti funkciją, kuri atlieka teksto suspaudimą. Funkcija priima vieną parametrą x - tekstas ir grąžina tekstą
    # sudarytą iš simbolio ir jo iš eilės einančių pasikartojimų skaičiaus t.y. suspaudimas vykdomas grupuojant iš
    # eilės einančius simbolius.
    try:
        x = str(input("Please enter a string: "))
    except ValueError:
        print("Invalid string")
        return

    def compress(x):
        count = 1
        newStr = ""
        for i in range(0, len(x)):
            if (i + 1 < len(x)):  # check if not last value
                if x[i] == x[i + 1]:  # if there is same char next then add 1 to count
                    count += 1
                else:  # if next value is different, then append to string that value and count
                    newStr += x[i]
                    newStr += str(count)
                    count = 1  # reset counter
            else:
                newStr += x[i]
                newStr += str(count)  # if there is only one in row then add char and add number
        return newStr

    print(compress(x))
    input()
    return


if __name__ == '__main__':
    while True:
        print(f'[1] First task\n[2] Second task\n[3] Third task\n[4] Fourth task\n[5] Fifth task\n\n[0] Exit')
        try:
            userInput = int(input('Enter your choice: '))
        except ValueError:
            print("Must be an integer!")
            break
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
