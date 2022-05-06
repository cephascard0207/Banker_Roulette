#Banker_Roulette
#Created with Python
#Day4 of 100DaysCodingChallenge
#Made with 💖 by Cephas Cardozo

#welcome_print
print("Welcome to the Banker Roulette")
print("Created by Cephas Cardozo \nDeveloped using Python\n")

#imports
import random

#global_variables
names_string = input("Give me everybodys names seperated by a comma to begin the game!\nType here: ")
names = names_string.split(",")
num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_pay = names[random_choice]

#print
print(person_pay.upper() + " will pay for the item.")