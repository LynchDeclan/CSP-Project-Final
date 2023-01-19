import sys
import random
import re
import time


# These three functions are for the title screens of each of the options. I call specific ones depending on the options
def title_one():
    print('  __  __          _____ _____ _____    ___        ____           ___    ___      ')
    print(' |  \/  |   /\   / ____|_   _/ ____|  / _ \      |  _ |    /\    | |    | |      ')
    print(' | \  / |  /  \ | |  __  | || |      | (_) |     | (_)|   /  \   | |    | |      ')
    print(' | |\/| | / /\ \| | |_ | | || |       > _ <  ___ |  _<   / /\ \  | |    | |      ')
    print(' | |  | |/ ____ \ |__| |_| || |____  | (_) |     | (_)| / ____ \ | |___ | |___ ')
    print(' |_|  |_/_/    \_\_____|_____\_____|  \___/      |____//_/    \_\|_____||_____| ')
    print('')


def title_two():
    print(' ____    _____   _____   _____       _____    ___   ___    ___    ')
    print('|  _  \ |_   _| / ____| | ____|     |  _  \  / _ \  | |    | |    ')
    print('| | | |   | |  | |      | |___      | (_) / | | | | | |    | |    ')
    print('| | | |   | |  | |      |  ___| --- | |\ \  | | | | | |    | |    ')
    print('| |_| |  _| |_ | |____  | |___      | | \ \ \ |_| / | |___ | |___ ')
    print('|____/  |_____| \_____| |_____|     |_|  \_\ \___/  |_____||_____|')
    print('')


def title_three():
    print('  _____   ___   _____   __  __       ______  ___      _____   ____  ')
    print(' / ____| / _ \ |_   _| |  \ | |     |  ____| | |     |_   _| |  _ \ ')
    print('| |     | | | |  | |   | \  \ |     | |____  | |       | |   | (_) | ')
    print('| |     | | | |  | |   | |\   | --- |  ____| | |       | |   | ___/  ')
    print('| |____ | |_| | _| |_  | | \  |     | |      | |___   _| |_  | |    ')
    print(' \_____| \___/ |_____| |_|  \_|     |_|      |_____| |_____| |_|    ')
    print('')


# The Magic 8-Ball option, with it's own code
def eight_ball():
    title_one()

    print('Hello and welcome to the magic 8-ball! Here, you can ask any Yes/No questions and we will give you your fortune!!!')

    # These varibles store the Magic 8-Ball's replies to the user
    answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely",
               "You may rely on it", "As I see it, yes", "Most Likely", "Outlook Good",
               "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later",
               "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
               "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very Doubtful", "No"]

    wants_ask = input('Do you wish to ask? [yes/no]: ')

    if wants_ask == 'no':
        chooser()

    # Check whether the user inputted an integer value
    if wants_ask == 'yes':
        question_number = 0
        while True:
            try:
                question_number = int(
                    input('How many times do you want to ask? (Number): '))
            except ValueError:
                print('Please enter an integer')
                continue
            else:
                print('You entered:', question_number)
                break

        # This chooses one of the strings in the variable "answers" by random
        for i in range(question_number):
            asking = input('What is your yes/no question?: ')
            print(random.choice(answers))
        print(' ')
        print(' ')


# The Diceroll option, with its own code
def dice_roll():
    title_two()
    print('Hello and welcome to the dice roll generator! Here you can ask what type of dice you want, and we will roll it for you!')
    print('You can also ask to roll multiple dice at once!')

    # These varieables store the numbers for each "side" of the dice
    roll_numbers_three = [1, 2, 3]
    roll_numbers_six = [1, 2, 3, 4, 5, 6]
    roll_numbers_twelve = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    roll_numbers_twenty = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                           10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    wants_roll = input('Do you wish to roll? [yes/no]: ')

    if wants_roll == 'no':
        chooser()

    diceroll_mode = input(
        'Please select a mode for rolling: [multiple/single]: ')

    # Runs if the user wants to roll a single die
    if diceroll_mode == 'single':
        # Check whether the user inputted an integer
        if wants_roll == 'yes':
            type_die = 0
            while True:
                try:
                    type_die = int(
                        input('Which type of dice would you like to roll? [3/6/12/20]: '))
                except ValueError:
                    print('Please enter an integer')
                    continue
                else:
                    print('Your', type_die, 'sided die results:')
                    break

        # Conditionals to check which type of "die" the user selected
        # Then pulled out a random value from whatever list of die "sides" corresponds
        if type_die == 3:
            print(random.choice(roll_numbers_three))

        if type_die == 6:
            print(random.choice(roll_numbers_six))

        if type_die == 12:
            print(random.choice(roll_numbers_twelve))

        if type_die == 20:
            print(random.choice(roll_numbers_twenty))

    # Runs if the user wants to roll multiple dice
    if diceroll_mode == 'multiple':
        # Check whether the user inputted an integer
        if wants_roll == 'yes':
            roll_number = 0
            while True:
                try:
                    roll_number = int(
                        input('How many times do you want to roll? (Number): '))
                except ValueError:
                    print('Please enter an integer')
                    continue
                else:
                    print('You entered:', roll_number)
                    break
        # Check whether the user inputted an integer
        if wants_roll == 'yes':
            type_die = 0
            while True:
                try:
                    type_die = int(
                        input('Which type of dice would you like to roll? [3/6/12/20]: '))
                except ValueError:
                    print('Please enter an integer')
                    continue
                else:
                    print('Your', type_die, 'sided die results:')
                    break

        # Conditionals to check which type of "die" the user selected
        # Pulls random values for the corresponding "side" of the die for however many time the user asked to roll
        if type_die == 3:
            for x in range(roll_number):
                print(random.choice(roll_numbers_three))

        if type_die == 6:
            for x in range(roll_number):
                print(random.choice(roll_numbers_six))

        if type_die == 12:
            for x in range(roll_number):
                print(random.choice(roll_numbers_twelve))

        if type_die == 20:
            for x in range(roll_number):
                print(random.choice(roll_numbers_twenty))


# The Coinflip option, with its own code
def coin_flip():
    title_three()
    print('Hello and welcome to the Coin Flipper! Here you can flip heads or tails, and you can also flip multiple times!')

    coin_flips = ["Heads", "Tails"]

    wants_flip = input('Do you wish to flip? [yes/no]: ')

    if wants_flip == 'no':
        chooser()

    coinflip_mode = input(
        'Please select a mode for flipping: [multiple/single]: ')

    if coinflip_mode == 'single':
        print(random.choice(coin_flips))
    print(' ')
    print(' ')
    if coinflip_mode == 'multiple':

        if wants_flip == 'yes':
            flip_number = 0
            while True:
                try:
                    flip_number = int(
                        input('How many times do you want to flip? (Number): '))
                except ValueError:
                    print('Please enter an integer')
                    continue
                else:
                    print('You entered:', flip_number)
                    break

            for x in range(flip_number):
                print(random.choice(coin_flips))
            print(' ')
            print(' ')


# Is the main function that makes the user choose what part of the program they would like to use
def chooser():
    option = input('Select an option [Magic8Ball/Diceroll/Coinflip/exit]: ')
    while option != 'exit':
        # These are the options the user can select, but they have to type in everything word-for-word, letter-by-letter, or it will not work
        if option == 'Magic8Ball':
            eight_ball()
        if option == 'Diceroll':
            dice_roll()
        if option == 'Coinflip':
            coin_flip()
    if option == 'exit':
        exit()


# Gives the user a guide on how to use this program
print('''
How to use this application:
When selecting inputs, make sure you know to type in one of the options that it presents
in the square brackets! Sorry, but we are also case-senitive!''')
print(' ')
chooser()
