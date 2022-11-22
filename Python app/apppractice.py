# print('Ayomide Ibitoye')
# print('0____')
# print(' ||||')
# print('*' * 10)

# price = 10
# rating = 4.9
# name = 'Ayo'
# is_published = False
# print(price)

# name = "John Smith"
# age = 20
# status = "new"
# print("We check in a patient named "+name+".")
# print("He's",age,"years old and is a",status,"patient.")

# name = input('what is your name? ')
# print('Hi '+name)

# name = input("what's your name? ")
# fav_color = input("what's your favorite color? ")
# print(name,'likes',fav_color)

# dob = int(input('Birth year: '))
# print(type(dob))
# age = 2022 - dob
# print(type(age))
# print(age)

# pounds = int(input('your weight in pounds: '))
# kilo = 0.45 * pounds
# print('your weight is ',kilo,'kilograms.')

# course = '''
# Hi Ayo,
#
# Here is our first email.
#
# thank you,
# the support team
# '''

# course = 'Python for Beginners'
# another = course[:]
# print(course[0:3])
# print(course[0:-1])
# print(another)

# first = 'Ayo'
# last = 'Ike'
# message = first+' ['+last+'] is a coder'
# msg = f'{first} [{last}] is a coder'
# print(message)
# print(msg)

# course = 'Python for Beginners'
# print(len(course))
# print(course.upper())
# print(course)
# print(course.lower())
# print(course.find('P'))
# print(course.replace('Beginners','Absolute Beginners'))
# print('Python' in course)

# import math as m
# x = 2.9
# print(m.ceil(x))
# help()

# hot_condition = False
# cold_condition = False
# if hot_condition:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif cold_condition:
#     print("It's a cold day")
#     print('Wear warm clothes')
# else:
#     print("It's a lovely day")
# print('Enjoy your day')

# price = 1000000
# good_credit = True
# print('Price of a house is $',price)
# if good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f"Down payment: ${int(down_payment)}")

# has_high_income = False
# has_good_credit = True
# if has_high_income or has_good_credit:
#     print("Eligible for loan")
# else:
#     print("not eligible")

# name = input("Input your name: ")
# if len(name) < 3:
#     print("Name nust be at least 3 characters.")
# elif len(name) > 10:
#     print("Name must be a maximum of 50 character.")
# else:
#     print("Name looks good")

# weight = int(input("Weight: "))
# unit = input('(L)bs or (K)g: ')
# k = 0.45 * weight
# l = weight / 0.45
# if unit.lower() == 'k' or unit.upper()== 'K':
#     print("you are",l,'pounds')
# elif unit.lower() == "l" or unit.upper()== 'L':
#     print("you are",k,'kilos')
# else:
#     print("Lbs or Kg?")

# i = 1
# while  i <= 5:
#     print('*' * i)
#     i = i + 1
# print("Done")

# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print('you won')
#         break
# else:
#     print('Sorry, you lost')

# my trial
# command = input("> ")
# help = '''start - to start the car
# stop - to stop the car
# quit - to exit
# '''
#
# input = ['help', 'start', 'stop', 'quit']
# while command == input:
#     if command == "help":
#         print(help)
# else:
#     print("I don't understand")
# print(help)

# correction
# command = ""
# started = False
# stopped = False
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             stopped = False
#             print("Car already started!")
#         else:
#             started = True
#             print("Car started...")
#     elif command == "stop":
#         if stopped:
#             started = False
#             print("Car already stopped!")
#         else:
#             stopped = True
#             print("Car stopped")
#     elif command == "help":
#         print('''start - to start the car
# stop - to stop the car
# quit - to quit
#         ''')
#     elif command == "quit":
#         break
#     else:
#         print("sorry i don't understand that")

# x = 27860400 / 30000
# print(x)

# For loops
# for item in range(5,10,2):
#     print(item)

# price = [10, 20, 30]
# sum = 0
# for item in price:
#     sum += item
# print(f"Total: {sum}")

# for x in range(4):
#     for y in range(3):
#         print(f"({x}, {y})")

# numbers = [2, 2, 2, 2, 5]
# for items in numbers:
#     x = ""
#     for x_count in range(items):
#         x += "x"
#     print(x)

# names = ['Ayo', 'Ike', 'John', 'Grace', 'Me']
# names[1] = 'Ikechukwu'
# print(names[1])

# My trial
# numbers = [1, 4, 3, 9, 7]
# max = max(numbers)
# print(max)

# Correction
# numbers = [1, 4, 3, 9, 7]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matrix[0][1])
# for row in matrix:
#     print(row)
#     for item in row:
#         print(item)

# numbers = [5, 2, 1, 7, 4]
# numbers.insert(0, 10)
# print(numbers)

# numbers = [5, 2, 7, 2, 5, 9]
# unique = []
# for number in numbers:
#     if number not in unique:
#         unique.append(number)
# print(unique)

# numbers = (1, 2, 3)
# print(numbers[0])

# Unpacking
# coordinates = (1, 2, 3)
# x, y, z = coordinates
# print(x)

# dictionaries
# customer = {
#     'name': 'Ayomide Ibitoye',
#     'age': 30,
#     'is_verified': True
# }
# print(customer['name'])

# phone_no = input('Phone: ')
# numbers = {
#     '1': 'One',
#     '2': 'Two',
#     '3': 'Three',
#     '4': 'Four',
#     '5': 'Five',
#     '6': 'Six',
#     '7': 'Seven',
#     '8': 'Eight',
#     '9': 'Nine',
#     '0': 'Zero'
# }
# output = ""
# for ch in phone_no:
#    output += numbers.get(ch, '!') + " "
# print(output)

# Emoji Converter
# message = input("> ")
# words = message.split(' ')
# emojis = {
#     ":)" : "Smiles",
#     ":(" : "Sad"
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)

# Functions
# def greet_user(first_name, last_name):
#     print(f'Hi {first_name}!')
#     print(f'Welcome aboard Mr. {last_name}')
# // always leave a two line space between your function call and your next line of code#
#
# print('Start')
# greet_user('Ayo', "ibitoye")
# greet_user('Ike', last_name='Sunday')
# print('Finish')

# Return Statement
# def square(number):
#     return number * number
#     # the Return statement is use in this code to remove the null/none response,
#     # Since by default a function returns none


# print(square(5))

# Creating a Reusable Function
# def emoji_converter(message):
#     words = message.split(' ')
#     emojis = {
#         ":)": "Smiles",
#         ":(": "Sad"
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output


# message = input("> ")
# print(emoji_converter(message))

# Exceptions => is a kind of error that crashes our code
# try, except => is a concept use to handle errors in the programs
# terminal or exceptions that are raised in our programs
# as a good we should always anticipate that

# try:
#     age = int(input("Age: "))
#     income = 20000
#     risk = income / age
#     print(risk)
# except ZeroDivisionError:
#     print('Age cannot be zero')
# except ValueError:
#     print('Invalid value')

# Comments
# used to highlight how's and why's
# they are not to tell what the next command is buh to tell how and why the code was written the way it is

# Classes => are used to define new types
# Pascal naming convention => is use to name classes,
# where the all first letters are capitalised and
# the underscore (_) is not used to seperate two words like
# the conventional method used in naming variables and functions (Eg. EmailClient)
# Object => is an instant of a class
# Points =>
# class Point:
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
#
# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()
#
# point2 = Point()
# point2.x = 1
# print(point2.x)


# Constructors => A constructor is a function that gets called at the time of creating an object
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def move(self):
#         print('move')
#
#     def draw(self):
#         print('Draw')
#
#
# point = Point(10, 20)
# print(point.x)
#
# Example
# class Person:
#     def __init__(self, name):
#         self.name = name

#     def talk(self):
#         print(f"Hi, I am {self.name}")
#
#
# ayo = Person("Ayomide")
# ayo.talk()
# print(f"Welcome {ayo.name}")
#
# ike = Person("Ikechukwu Sunday")
# ike.talk()


# Inheritance => Is a mechanism for reusing code as the name implies,
# it is used to pass down features from one class to another
# class Mammal:
#     def walk(self):
#         print("Walk")
#
#
# class Dog(Mammal):
#     def bark(self):
#         print("Bark")
#
#
# class Cat(Mammal):
#     pass
#
#
# dog1 = Dog()
# dog1.walk()


# Modules => Is basically a file with Python code,
# It is used to organize our code into multiple files
# Import => is used to call a module into a code
# Modules =>
# import utils
# from utils import kg_to_lbs
#
# print(kg_to_lbs(100))
#
# print(utils.kg_to_lbs(72))

# import utils
# numbers = input([ int | slice])
# num = numbers.split(" ")
# maximum = utils.find_max(num)
# print(maximum)

# Packages => is a directory or folder,
# and its another way to organize our programme.
# it is a container for multiple modules
# methods of importing modules and functions in a packages, method 1:
# import ecommerce.shipping
# ecommerce.shipping.calc_shipping()
# method 2 (this method is used when you want to access all the function from a module in a package)
# from ecommerce import shipping
# shipping.calc_shipping()
# method 3 (this method is used when you want to access only one function from a module in a package)
# from ecommerce.shipping import calc_shipping
# calc_shipping()
# Method 4 (when you want to access multiple function without calling the entire module)
# from ecommerce.shipping import calc_shipping,calc_tax
# calc_shipping()
# calc_tax()

# Generating Random Values =>
# How to use one of the built-in module to Generate Random Values
# import random
# for i in range(3):
#     print(random.random())
#     print(random.randint(10,20))

# members = ['Ike', 'Ayo', 'Mosh', 'John']
# leader = random.choice(members)
# print(leader)

# Exercise,
# first attempt
# import random
# dice = range(1,6+1)
# i = random.choice(dice)
# j = random.choice(dice)
# roled = (i, j)
# print(roled)

# second attempt
# import random
#
# class Dice:
#     def roll(self):
#         dice = range(1, 6 + 1)
#         i = random.choice(dice)
#         j = random.choice(dice)
#         roled = (i, j)
#         return roled
#
#
# roles = Dice()
# print(roles.roll())

# correction
# import random
#
#
# class Dice:
#     def roll(self):
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         return (first, second)
#
#
# dice = Dice()
# print(dice.roll())

# Files and Directories
# pathlib => It provides an Object-oriented filesystem paths,
# which means provides classes that we can use to create objects,
# to work with directories and files.
# the Path class is found in pathlib.
# A Path object is used to reference a file or directory on a computer,
# and there are basically 2 ways to do it.
# we can use an Absolute Path; is a path that start from the root of our hard-disc,
# eg. c:\program files\microsoft
# or a Relative Path; is a path starting from the current directory
# buh in this tutorials we'll work with the Relative path
#
# from pathlib import Path
# path = Path()
# print(path.exists())  # to check if a file or directory exist
# print(path.mkdir())  # to make or create directory
# print(path.rmdir())  # to remove or delete directory
# print(path.glob('x.py'))  # to search for files and directories in the current path
# for file in path.glob('* '):
#     print(file)

# x = 2000 * 2701 + 3000 * 531
# print(x )

from __future__ import division

users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klien"}
]

friendship = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (3, 5), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for user in users:
    user["friends"] = []

for i, j in friendship:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])


def number_of_friends(user):
    """how many friends does_user_have?"""
    return len(user["friends"])


total_connections = sum(number_of_friends(user)
                        for user in users)
# print(total_connections)

num_users = len(users)
avg_connections = total_connections / num_users
# print(avg_connections)

num_friends_by_id = [(user["id"],
                      number_of_friends(user))
                      for user in users]
num_friends = []

# sorted(num_friends_by_id,
#        key = lambda(user_id, num_friends): num_friends,
       # reverse = True)

