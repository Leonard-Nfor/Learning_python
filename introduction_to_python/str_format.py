#!/usr/bin/python3

"""here how string were being format in older version of python"""

name = "Leonard"
age = 26

print("Hello, %s. You are %s years." % (name, age))

""" Later on str.format was introduce in python 2.6"""

print("Hello, {}. You are {} years now!".format(name, age))

"""You can reference variables in any order by referencing their index"""

print("Hello, {1}. You are {0} years now!".format(age, name))

"""dictionary can also be used by referencing their keys in paranthesis 
while unpacking with **"""

person = {'name' : 'Leonard', 'age' : 26}

print("Hello, {name}. You are {age} year now! so you are getting older".format(**person))

""" improvement again, so we can pass the variable direct to f-string without mentioning format"""

print(f"Hello, {name}. You are {age} years now!")
