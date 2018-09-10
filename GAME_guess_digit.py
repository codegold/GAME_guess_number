import random
guessesTaken = 0
print('Hello what is your name?')
my_name = input()
number = random.randint(1,20)
print('Ok, '+ my_name +' ill guess a number from 1 to 20.')

for guessesTaken in range(6):
    print('Try to guess.')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your number is too low.')

    if guess > number:
        print('Your number is too high')

    if guess == number:
        break

if guess == number:
    guessesTaken =  str(guessesTaken + 1)
    print('Great '+ my_name +' ! You did it for ' + guessesTaken + ' try!')

if guess != number:
    number = str(number)
    print('Alas, I made a guess ' + number + '.')