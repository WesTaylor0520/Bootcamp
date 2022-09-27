def calculator_if_else_elif():
    first_number = int(input("Enter a first number:"))

    second_number = int(input("Enter a second number:"))

    operator = input("Select an operator:")

    if operator == "+":
        print("Addition " + str(first_number + second_number))
    elif operator == "-":
        print("Subtraction " + str(first_number - second_number))
    elif operator == "*":
        print("Multiplication " + str(first_number * second_number))
    elif operator == "/":
        print("Division " + str(first_number / second_number))
    elif operator == "//":
        print("Modulo " + str(first_number % second_number))


def username_cool_or_not():
    username = input("Gimme your name:")

    if username == "wes":
        print("You the king boi")
    elif username == "Dexter":
        print("not bad but not good")
    else:
        print("Don't recognise you cool kids")


# username_cool_or_not()


def list_exercise():
    fruits = []
    fruit = ""
    while fruit != "quit":
        fruit = input("Enter the name of a fruit: ")
        if fruit != "quit":
            fruits.append(fruit)

    for fruit in fruits:
        print(fruit)


list_exercise()