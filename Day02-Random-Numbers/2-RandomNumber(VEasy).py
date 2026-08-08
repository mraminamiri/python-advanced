from random import random , randrange
#Version 1

for i in range(3):
    print(randrange(100,999,5),end=',')



#Version 2
import random

numbers = []

while len(numbers) < 3:
    number = random.randint(100, 999)

    if number % 5 == 0 and number not in numbers:
        numbers.append(number)

print("Generated numbers:")

for number in numbers:
    print(number)

