import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}'))
        if guess > random_number:
            print('Sorry your guess is too high')
        elif guess < random_number:
            print('Sorry your guess is too low')
    print(f'yaay you guessed correct number {random_number}')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # because low=high
        feedback = input(f'Is{guess} too high(h), too low (l)or Correct (c)')
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'yay! The computer guessed your number {guess}, correctly')


computer_guess(1000)
