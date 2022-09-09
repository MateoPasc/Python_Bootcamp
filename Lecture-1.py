
# This is a comment

print("Hello, World!")

a = 15.9
b = 6

print('a = ', a)
print('b = ', b)

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a/b)

print("Integer division:", a//b)
print("Modulo:", a%b)

print("a squared:", a**2)
print("a cubed", a**3)
print("a^9", a**9)

print("sqrt(2)", 2**(1/2))

c = round(1.1/3, 3)
print("Rounding", c)

########################################

print("Before", a, b)

# Swap variables
a, b = b, a

print("After", a, b)

########################################


name = 'Monty Python'
title = "Holy Grail"  # Python doesn't care between " " and ' '.

print(name)
print(title)

full_title = name + " and the " + title
print(full_title)

# First character
print(name[0])

# Last character
print(name[-1])

print(name[0:5])
print(name[6:])
print(title[:4])

# Every other character
print(name[::2])
print(name[1::2])
print(name[1:8:2])

# Modifying strings
print(title[:-1] + 'n')

# String length
print("Length:", len(name))

print('First line\nSecond line')

print("Hello! "*10)

# Counts the number of n's in name
print(name.count('n')) # case sensitive

# Replacing a substring
print(name.replace('o', 'a'))

########################################

# Type conversions
x = "3.14"
y = float(x)
z = int(y)

print(x, y, z)

print (z +1 )


########################################
# What will this code print out:
a = 'rosemead'
b = 'new york'

print(a[2:5] + b[4:] + 'a')

########################################


# Lists - ultimate containers!

apollo_moon = [11, 12, 14, 15, 16, 17]

print(apollo_moon)

apollo_commanders = ["Armstrong", "Conrad", "Shephard", "Scott", "Young", "Cernan"]

print("Post-Apollo 13 Commanders:", apollo_commanders [2:])

apollo_commanders[0] = "Lovell"
print(apollo_commanders)

# Appending an entry
apollo_moon.append(18)
apollo_moon.append(19)

print("Added cancelled missions:", apollo_moon)

# Popping last entry 
last_cancelled = apollo_moon.pop()
print(last_cancelled)
print(apollo_moon)

# Insert the failed Apollo 13 mission
apollo_moon.insert(2, 13)
print(apollo_moon)

# Removing by value
apollo_moon.remove(13)
print(apollo_moon)

# Removing by index (same as popping last entry)
apollo_moon.pop(-1)
print(apollo_moon)


print("Index of Apollo 11:", apollo_moon.index(11))

# Reversing a list (in place)
apollo_moon.reverse()
print("Reverse:", apollo_moon)

# Reversing a list without modifying it
print ("Back to normal:", apollo_moon[::-1])

########################################

apollo12_crew = ["Pete", "Rick", "Al"]
commander, cm_pilot, lm_pilot = apollo12_crew
print(commander, cm_pilot, lm_pilot)

# 2D list
list2D = [[1, 2], [3, 4]]
print(list2D)

# Accessing elements of multi-dimensional lists
print(list2D[0][1])

# Weird lists
mission_details = [1969, 'Apollo 12', ['Conrad', 'Gordon', 'Bean'], 10.19194]
print(mission_details)

print(lm_pilot, mission_details[2][2])


########################################

ww2 = [1939, 1940, 1941, 1942, 1943, 1944, 1945]

ww2 = map(str, ww2)
print(ww2)

# Joining list elements by a delimiter
print(', '.join(ww2))


########################################

# QUESTION 2
# What will this code print out:

a = [1, 2, 3, 4]
b = ['10', '11', '12', '13']
print(int("5" + b[-1]) + a[1])






########################################

x = [1, 2, 20, 21, 22, 23, 1, 1]


print(sum(x))

print(max(x))
print(min(x))

print(x.count(1))

# Sorting in place
x.sort()
print(x)

# Reversing a list in place
x.reverse()
print(x)

print(sorted(x).reverse())

########################################

# Lists: shallow VS deep copy

a = [1, 2, 3, 4]

# Shallow copy - doesn't copy a to b, it only passes a reference to a

b = a

print(a, b)

a[0] = 100
print(a, b)


# Deep copy - create a new list
b = list(a)

a[0] = 0

print(a, b)


# Dictionaries
phonebook = {}
phonebook["holmes"] = ["Sherlock", "221B Baker Street", "London"]
phonebook["potter"] = ["Harry", "4 Privet Drive", "Surrey", 442357896585]

print(phonebook['holmes'][1])

phonebook = {}

phonebook["holmes"] = {
    'name': "Sherlock",
    'address': "221B Baker Street",
    'city': "London",
    'country': "UK",
    'tel': 4421458751
}

print(phonebook['holmes']['city'])


########################################

# Input

a = input("Enter:")

print(a)

a = int(input("Enter:"))
if a > 10:
    print('yay!')
else:
    print("nooooo")


########################################

# Rock, Paper, Scissors game


P1 = input('Player 1: ')
P2 = input('Player 2: ')

outcomes = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}

P1 = outcomes[P1]
P2 = outcomes[P2]

c1 = 1
c2 = -2

if P2 - P1 == 1 or P2 - P1 == -2:
    print("Player 2 wins!")

if P2 - P1 == -1 or P2 - P1 == 2:
    print("Player 1 wins!")

if P2 == P1:
    print("It's a tie!")

