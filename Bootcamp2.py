import time


def question():
    answer = input("Hello please can you select one of the following options \n"
                   "1 - Enter name and surname \n"
                   "2 - Greeting message \n"
                   "3 - Quit \n")
    return answer


def response_1():
    first = input("Please enter your first name: ")
    second = input("Please enter your second name: ")
    print("Thank you, taking you back to the main menu \n")
    time.sleep(2)
    return first, second


def response_2(first_n, second_n, greeting):
    print(greeting)
    updated_greeting_message = greeting
    if first_n == "":
        time.sleep(2)
        print("To change default greeting please enter name and surname first \n")
        time.sleep(2)
    else:
        change_greeting = input("Would you like to change your greeting message? \n"
                                "Please enter Y to change or N to not: ")
        if change_greeting == "Y":
            new_greeting = input("Please choose a greeting message: ")
            updated_greeting_message = new_greeting + ' ' + first_n + ' ' + second_n
            print(updated_greeting_message + "\n")
            time.sleep(2)
            print("Thank you, taking you back to the main menu \n")
            time.sleep(2)
        else:
            print("No worries")
            time.sleep(2)
            print("Thank you, taking you back to the main menu \n")
            time.sleep(2)
    return updated_greeting_message


first_name = ""
second_name = ""
greeting_message = "Welcome"
program = True
while program:
    response = question()

    if response == "1":
        first_name, second_name = response_1()

    if response == "2":
        greeting_message = response_2(first_name, second_name, greeting_message)

    if response == "3":
        program = False
