# Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year that they will turn 100 years old.

import datetime

#variables
now = datetime.datetime.now()

#input
name = input("What is your name: ")
age = int(input("and your age: "))

#math
year = str((now.year - age) + 100)

#output
print("Hello {name} you're gonna be 100 in {year}".format(name, year))
