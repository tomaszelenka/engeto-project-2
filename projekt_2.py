'''
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Tomáš Zelenka
email: me@tomaszelenka.cz
discord: .toze.
'''

import random


#VALIDATE USER INPUT
def validate_user_input(guess):

    if len(guess) != 4:
        print("Please enter a four-digit number.")
        return False

    if len(set(guess)) < 4:
        print("Please enter a number without duplicate digits.")
        return False

    if guess[0] == '0':
        print("The number must not start with zero.")
        return False

    if not guess.isdigit():
        print("Please enter a number without non-numeric characters.")
        return False

    return True

#GET UNIQUE NUMBER
def unique_number():
    unique_numbers = []
    while len(unique_numbers) < 4:
        number = random.randint(1, 9)
        if number not in unique_numbers:
            unique_numbers.append(number)
    return unique_numbers

#GET BULLS
def bulls(sel):
    x = 0
    bullsn = 0
    for i in sel:
        if i == to_compare[x]:
            x+=1
            bullsn+=1
        else:
            x+=1
    return bullsn

#GET STATISTIC
def statistics(number_success):
    if number_success == 0 or number_success == 1:
        print("Wow, that's amazing")
    elif number_success <= 5:
        print("That's average")
    else:
        print("That's not so good")      


#GET COWS
#It works even with other cases, like having a duplicate number in user input
def cows(sel):
    x = 0
    counter_result = 0
    exclude = []
    for i in sel: 
        if i in to_compare and i == to_compare[x]:
            exclude.append(i)
            x+=1
            continue
        elif (i in to_compare and i != to_compare[x]) and (i in exclude):
            x+=1
            continue
        elif (i in to_compare and i != to_compare[x]) and (i not in exclude):
            counter_result+=1
            x+=1
            continue
        else:
            x+=1
    exclude.clear()
    return counter_result

line = "-----------------------------------------------"

# SAVE UNIQUE NUMBER
to_compare = unique_number()
#print(to_compare) #SHOW UNIQUE NUMBER

#WELCOME BOARD
print("Hi there")
print(line)
print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
print(line)

#CHECK VALIDATE INPUT
while True:

    user_number = input("Enter a number:")
    print(line)

    if validate_user_input(user_number):
        break

#USER INPUT TO LIST-INT
sel_compare = []
for i in user_number:
    sel_compare.append(int(i)) 

# CHECK COMPARE
first_input = True
count_static = 0
while sel_compare != to_compare:
       
    if not first_input:
        while True:
            user_number = input("Enter a number:")
            print(line)

            if validate_user_input(user_number):
                count_static+=1
                sel_compare.clear()
                for i in user_number:
                    sel_compare.append(int(i)) 
                break

    else:
        first_input = False
  
    #SHOW BULLS and COWS
    count_bulls = bulls(sel_compare)
    count_cows = cows(sel_compare)

    bulls_message = f"{count_bulls} {'bull' if count_bulls == 1 else 'bulls'}"
    cows_message = f"{count_cows} {'cow' if count_cows == 1 else 'cows'}"

    print(f"{bulls_message}, {cows_message}")
    print(line)

    
else:
    print("Correct, you've guessed the right number")
    print(line)
    statistics(count_static)

