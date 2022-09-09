

def addNums(a, b):
    """" Adds two numbers.

    Arguments:
        a: [int/float] Number 1.
        b: [int/float] Number 2.

    Return:
        [int/float] The sum.

    """

    c = a + b

    return c

# Calling a function
print(addNums(5, 8))

# Example input: HH:MM:SS --> HH.hhhh
def decimalHour(time_string):
    """" Converts time from the 24hrs hh:mm:ss format to decimal hour. """

    hh, mm, ss = time_string.split(":")

    hh, mm, ss = map(float, (hh, mm, ss))

    result = (ss/60 + mm)/60 + hh

    return result

print(decimalHour("05:29:45"))

print(decimalHour)


def utcDecimal(time_string, timezone=0):   # timezone=0 is the default value. If not inputted, assumes timezone is 0.
    """" Converts time from the 24hrs hh:mm:ss format to decimal hour, with respect to timezone. """

    result = decimalHour(time_string) + timezone

    return result%24

print(utcDecimal("05:29:45"))
print(utcDecimal("05:29:45", -7))


# Local and global variables

var = 5

def test(var):
    print("Input:", var)

    var = 20

    print("Changed:", var)

var = 10

test(var)
# It doesn't matter where the function/def is defined, it is run in the instance it is called
# by the code and takes the input value defined last, like in this example.

print("Global:", var)

# Unpacking function arguments from a list

def isTriangle(a, b, c):
    """" Checks if the given triangle sides can form triangle. """

    if c > (a + b):
        return False

    elif b > (a + c):
        return False

    elif a > (b + c):
        return False

    
    return True     # Note you don't need the "else"


triangle_sides = [2, 3, 4]

print("Is ", triangle_sides, "a triangle:",  isTriangle(*triangle_sides))  # the * unpacks the list into its elements


#######################################


from turtle import color
import numpy as np

# 2 points in 3D space
a = [[5, 1, 8], [3, 4, 6]]

print(a)

a = np.array(a)

print(a)

print("Shape:", a.shape)   # numpy arrays are proper, like matrices and unlike lists.
print("Dimensions:", a.ndim)
print("Type:", a.dtype)
print("Total number of elements:", a.size)


# Array of zeros
b = np.zeros((3, 3))

print(b)
print(b.dtype)

# An array of 1s, forcing the type to int
c = np.ones((3, 3), dtype=np.int32)

print(c)

# Identity matrix
idm = np.eye(3)
print(idm)


# Converting the string list to a float list
num_lst = ["1.20", "2.15", "3.78", "4.05"]
num_lst = np.array(num_lst).astype(np.float64)
print(num_lst)

# Creating an array of numbers from 0 to 100 as an array, with a step of 0.5

arr = np.arange(0, 100, 0.5)

print(arr)

# Creating a range of numbers - another approach
arr2 = np.linspace(0, 2, 9)
print(arr2)

# Reshaping an array
arr2 = arr2.reshape((3, 3))

print(arr2)


### Operations between arrays/matrices

a = np.zeros((3, 3))

# Adding a scalar to an array
a = a + 5
print(a)

# Multiplying by a scalar
a *= 3
print(a)

# Raising to a power. Individual elements are raised, not the matrix
a = a**2
print(a)


a = np.zeros((3, 3)) + 2
b = np.zeros_like(a) + 3

# Multiplying matrices, element-wise
print(a * b)

# Dot product (matrix product)
print(np.dot(a, b))

# Some other operators
a = np.arange(1, 101)
print(np.sum(a))
print(np.min(a))
print(np.max(a))
print(np.mean(a))
print(np.median(a))
print(np.std(a))
print("{:.2f}".format(np.std(a)))


#######################################

arr = np.linspace(1, 5, 20)

print(np.sqrt(arr))
print(np.sin(arr))
print(np.cos(arr))
print(np.exp(arr))

#######################################

# MATPLOTLIB

import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
# y = np.sin(x)

plt.plot(x, np.sin(x), color='red', linestyle='--', label='Sine')
plt.plot(x, np.sqrt(x), color='g', linewidth=10, label="Square Root")
plt.plot(x, np.tan(x), color='#FFD700', linestyle='', marker='o', label='Tan')
# plt.plot(x, np.zeros_like(x) + np.mean(y) + np.std(y), linestyle='--', color='red')

plt.legend(loc='upper left')

plt.title("My frist plot")
plt.xlabel("X")
plt.ylabel("Y = sin(X)")

plt.xlim((0, 5))
plt.ylim((-2, 2))

plt.grid()

plt.show()



#######################################

# QUIZ 4

# 3 quiestion, all programming

# Q1 write a function. Create a doc string explaining function.
# Q2
# Q3 Use Numpy or other to generate random numbers (prev. lecture)
#    Synthesis of all lectures. Work on that data set and answer a
#    couple of questions on that data set. Make a plot on that data
#    set. To do plot, google instructions.