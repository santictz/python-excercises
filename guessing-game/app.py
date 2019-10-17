# This script will generate a random number between 0 and 9
# and the user must guess having 3 tries
import random
secret_number =  random.randint(0, 9)
tries = 3

print('Guess the secret number!')
while tries > 0:
    guess = int(input('Guess: '))
    tries -= 1
    if guess == secret_number:
        print('You won!')
        break
    elif tries > 0:
        print(f'Incorrect. You still have {tries} tries!')
else:
    print(f'You lose. The number was {secret_number}')
    