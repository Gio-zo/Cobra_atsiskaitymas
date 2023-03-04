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


# Task 3 functions


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


# Main function

print("Welcome to tasks")
while True:
    try:
        print("Please select from following menu:\n"
              "[1] - task 1 (value of a string)\n"
              "[2] - task 2 (actions with list)\n"
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
            print("To modify values of list please visit our code (line 90)")
            # Feel free to modify this list in order to change program output
            input_list = [
                [1, 10, 34, 110, 400, 30, 20],
                [-5, -10, 55, 120, 30],
                [2, 67, 23, 78, 200],
            ]
            print(f'List: {input_list}')
            list_parser(input_list)


        elif choise == 3:
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

        elif choise == 4:
            break

        elif choise == 5:
            break

        else:
            raise ValueError

    except ValueError:
        print("Wrong value entered... Try again!")
        input()
    except SyntaxError as e:
        print(f"Error: Invalid syntax in input list in Task2 at line {e.lineno}")
        input()
