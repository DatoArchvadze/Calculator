import math

def prompt():
    try:
        pos_operations = ['+', '-', '*', '/', 'power']
        first_user_num = float(input('please enter first number --> '.title().strip()))
        operation = input('please enter operation + or - or * or / or power -->'.title().strip())
        second_user_num = float(input('please enter second number --> '.title().strip()))

        if operation == "+":
            print(f"your answer is : {first_user_num + second_user_num}")
        elif operation == "-":
            print(f"your answer is : {first_user_num - second_user_num}")
        elif operation == "*":
            print(f"your answer is : {first_user_num * second_user_num}")
        elif operation == "/":
            print(f"your answer is : {first_user_num / second_user_num}")
        elif operation == "power":
            square = math.pow(first_user_num, second_user_num)
            print("your answer is : {}".format(square))
        elif operation not in pos_operations:
            print('please follow rules !!! \U0001F624'.upper())
            prompt()
    except:
        print("\nsomething wrong!sorry try again :) \n please follow rules".title())
        prompt()
def ask_for_new_calculate():
    global a
    a=str(input('do you want another calculate? --> '.title().strip())).lower()
while True:

    prompt()
    ask_for_new_calculate()

    if a == "no":
        print("thanks for using this program \U0001F496 \n bye".title())
        break
    elif a=="yes":
        print("Ok,here we go again \U0001F606".title())
    else:
        a=str(input("please enter yes or no -->".title()))
        if a=="no":
            print('Ok,thanks for use this program \U0001F496')
        elif a=='yes':
            print("Ok,here we go again \U0001F606".title())
            prompt()
        else:
            ask_for_new_calculate()