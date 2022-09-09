

# While loop

# Fibonacci series
from asyncore import read
import doctest
from unittest import result


a, b = 0, 1
while b<100:
    print(b, end=',')
    a, b = b, a + b

print()

# DO NOT do an Infinite loop

# while 1:
#     # Do nothing
#     pass

############################

a = 10
if a%2 == 0:
    print('even number!')
else:
    print('odd number!')

if a <= 10:
    print("less than or equal to 10")
else:
    print("greater than 10")

# Relational operators:
# == equal to
# != not equal to
# < less than
# > greater than
# <= 
# >=

print(8==8)
print(1==2)
print(True == 1)        # True has value 1  
print(False == 0)       # False has value 0

var = None              # None is not just 0, but "empty"

if var is None:
    print("The variable is None!")



# Combining conditions - airplane edition
age = 8

if age < 2:
    print ("Free fare!")

elif (age >= 2) and (age < 12):
    print ("50% off")

else:
    print("Full fare!")


# Logical operators 2:
# not, and, or, "xor" - (one or the other but not both) 


# Testing strings

test_str = "It is not safe to go alone. Take this!"

if "safe" in test_str:
    print('We have "safe"')

    test_list = [1, 2, 3.14, 4]

    if 3.14 in test_list:
        print(test_list)


# List as condition
test_list = ['abc', 1, 87.254]

if len(test_list):
    print("Th lsit is not empty")
else:
    print("The list is empty")

############################

# QUESTION 1
# What does this code print out?

x = 81

if (x%2 == 0) and (x > 100):
    print("Alpha")

elif ((x%3 == 0) and not (x%9 == 0)):
    print("Kilo")

elif ((x%5 == 0) or ((x-1)/10 < 10)):
    print("Delta")

else:
    print("Echo")


############################

# Find the smaller number divisible by 2, 3 and 7
x = 7
while x < 100:

    if (x%2 == 0) and (x%3 == 0) and (x%7 == 0):
        print (x)

        break

    x +=1       # Adds +1 to x


############################


# Leap year:
# - evenly divisible by 4
# - if divisble by 100, it is NOT a leap year, except...
# - if it is also divisible by 400, then it IS a leap year

x = 1990
while x < 2030:

    if ((x%4 == 0) and (x%100 != 0)) or (x%400 == 0):
        print(x, "is a leap year")

    else:
        print(x)
    
    x += 1


############################

# For loop

# First 50 numbers in Fibonacci series
a, b = 0, 1
for i in range (50):
    print(b, end=', ')
    a, b = b, a + b

print()

cities = ['New York', 'Paris', 'Peckham']
for city in cities:
    print(city)


for i, city in enumerate(cities):
    print(i, city)

countries = ['USA', 'France', 'UK']
for country, city in zip(countries, cities):
    print(country, city)

############################

# QUESTION 2
# You are reading someone's spaghetti code,
# and you see this little gem. What does it do?

data = [
    [65.90, 432.6],
    [12.40, 76.30],
    [12.45, 90.80],
    [57.40, 47.20]
]

var = 0
for x, y in data:

    if x > y:
        var += x
    else:
        var += y
    
print(var/len(data))


############################

### READING FILES

file_name = 'data.txt'

with open(file_name, 'r') as f:

    print(f.closed)     # Tells us if f is open to read or closed

    print(f.readline())


# The file is now closed out here
print(f.closed)

# Reading now doesn't work
# print(f.readline())

# Reading the file line by line
with open(file_name) as f:

    for line in f:
        print(line)


# Splitting a string by a delimiter
a = 'one,two,three,four'
print(a.split(','))

# Stripping whitespace
b = '        center      '
print(b.strip())

# Printing file contents as a list
with open(file_name) as f:
    for line in f:

        #  Remove newline char \n
        line = line.replace('\n', '')

        # Convert into a list
        line = line.split(',')

        print(line)


############################

# QUIZ QUESTIONS:

# Q1 Do Loops: order in which things are being read
# Q2 if with couple of conds. Tell result
# Q3 Lists: conds, how to use list in
# Q4 Files: reading and parsing (end of lecture)
# Q5 For loop: Discuss what that loop does
# Q6 Review Leap year section

# One question involves writing and testing a script