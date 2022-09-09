# QUIZ 4

#############################

# Q1

def kineticEnergy(mass, vel):
    """ Calculate the kinetic energy given by KE = 1/2*m*v^2. Output is in Joules if units of inupt values are\
        kg for 'mass' and m/s for velocity 'vel'. """

    KE = 0.5*mass*vel**2

    return KE

bullet = [0.05, 1200]
meteor = [0.00005, 60000]

print("Kinetic energy of bullet is ", "{:.0f}".format(kineticEnergy(*bullet)), "J")
print("Kinetic energy of meteoroid is ", "{:.0f}".format(kineticEnergy(*meteor)), "J")




#############################

# Q2

def decimalDegrees(degree_string):
    """" Converts geographical coordinates from the sexagesimal DDdMMmSSs format (degrees, minutes, seconds) to decimal degrees format.\
        Each degree has 60 minutes and each minute has 60 seconds. """

    dd, mm, ss = degree_string[0:2], degree_string[3:5], degree_string[6:8]

    dd, mm, ss = map(float, (dd, mm, ss))

    result = (ss/60 + mm)/60 + dd

    return result

print(decimalDegrees("25d34m59s"))


#############################

# Q3 part a)

# Write a program which draws 200 samples from a Gaussian distribution (mean = 75, standard deviation = 5).
# Use the random.gauss function from the random library.
# Imagine these numbers represent final grades of students in a course.

# Tasks:
# a) Print how many students failed the course (grade < 50) and how many got an A (grade > 90). (1 point)

import random

gradebook = []
failures = 0
As = 0


for _ in range(200):

    grade = random.gauss(75, 5)

    if grade < 50:
        failures += 1

    elif grade > 90:
        As += 1

    gradebook.append(grade)

print(failures, " students failed.")
print(As, " students got an A.")



#############################

import random
import numpy as np

gradebook = [random.gauss(75, 5) for _ in range(200)]  # "List comprehension": For-loop inside list generating sample.

gradebook = np.array(gradebook)

failures = gradebook[gradebook < 50].size
As = gradebook[gradebook > 90].size


print(failures, " students failed.")
print(As, " students got an A.")

#############################

# Q3 part b)

# b) Plot a histogram of the student grades. Label the x-axis "Grade" and the y-axis "Students". (2 point)

import matplotlib.pyplot as plt


plt.hist(gradebook, bins=[0, 50, 60, 70, 80, 90, 100], edgecolor='grey')

plt.title('Histogram of grades')

plt.show()


# Unfortunately I ran out of time and could not submit part b) in time.