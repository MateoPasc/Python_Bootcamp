###################
# Q1
numbers = [10, 20]
items = ["Wave", "Particle"]

for x in numbers:
  for y in items:
    print(x, y)

###################
# Q2
x = 5
if x < 5:
    x += 2
else:
    x += 4

if x >= 8:
    x = x + 1

print(x)

###################
# Q3

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

if 11 in primes:
    print('yes')

###################
# Q4

line = '1,2,3,4,5'

line = line.split(',')
print(line)

###################
# Q5

n = 0
for x in range(1, 100):
    n += x

    print(x, n)



print()
print()

###################
# Q6

StNum = 18

for x in range(1,StNum+1):
    if (x%3 == 0) and (x%5 == 0):
        print('FizzBuzz')
    elif (x%3 == 0):
        print('Fizz')
    elif (x%5 == 0):
        print('Buzz')
    else:
        print(x)

