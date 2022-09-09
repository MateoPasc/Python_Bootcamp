# Q1

x = 2.718281828459

print("{:.3f}".format(x))

#######################################
# Q2

with open("output.txt", 'w') as f:
    f.write("1\n")

with open("output.txt", 'a') as f:
    f.write("2")


#######################################
# Q3

import math
import random

N = 10
circle_count = 0

for _ in range(N):
    x = random.random()
    y = random.random()

    if math.sqrt(x**2 + y**2) < 1:
        circle_count += 1

ratio = circle_count / N

pi = 4 * ratio

print("Pi is estimated to be " + str(pi))

#######################################

# Part b
# Trying to find when 10/10 we get 3.14 at least

magnitude_order = 0

ConsistentPi = 3.14

consistency_count = 0

while consistency_count != 10:

    N = 10**magnitude_order

    circle_count = 0

    for _ in range(N):
        x = random.random()
        y = random.random()

        if math.sqrt(x**2 + y**2) < 1:
            circle_count += 1

    ratio = circle_count / N

    est_pi = 4 * ratio

    if int(100 * est_pi) - 100 * ConsistentPi == 0 :
        
        consistency_count += 1

    else:

        consistency_count = 0

        magnitude_order += 1
            

print("To consistently obtain 3.14 as an estimate of Pi to 2 d.p., N must be of magnitude order "\
      + str(magnitude_order) +".")