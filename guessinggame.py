import random
print('Number guessing game')
print('Rules:')
print('1. The number is between 1 and 9')
print('2. You have 5 chances only')
print('GOOD LUCK!!! 🍀')
number = random.randint(1, 9)
chances = 0
while (chances<5):
    guess = int(input('Guess a number between 1 and 9: '))
    if (guess>number):
        print('Your guess is too large. Try a smaller number')
    elif (guess==number):
        print('You guessed the number! Congratulations! 👏 🥳')
    else :
        print('Your guess is too small. Try a larger number')
    chances = chances+1
if (chances>5):
    print('Oh no! You are out of chances. Try playing again')