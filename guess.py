# Concepts: Random module, for loop, f strings

import random

num = random.randint(1,10)

for i in range(0,3):
    user = int(input('Guess the number: '))

    if user == num:
        print('Hurray!')
        print(f'You guessed the number right! It\'s {num}')
        break


if user != num:
    print(f'Your guess is incorrect! The number was {num}')