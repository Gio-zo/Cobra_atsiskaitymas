# Functions that are used in code:
# Task 1 functions
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


# Task 2 functions

print("Welcome to tasks")
while True:
    try:
        print("Please select from following menu:\n"
              "[1] - task 1 (value of a string)\n"
              "[2] - <coming soon>\n"
              "[3] - <coming soon>\n"
              "[4] - <coming soon>\n"
              "[5] - <coming soon>\n"
              "[0] - exit program\n")
        choise = int(input("You choose:"))

        if choise == 0:
            print("Bye!")
            break

        elif choise == 1:
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

        elif choise == 2:
            break

        elif choise == 3:
            break

        elif choise == 4:
            break

        elif choise == 5:
            break

        else:
            raise ValueError

    except ValueError:
        print("Wrong value entered... Try again!")
        input()
