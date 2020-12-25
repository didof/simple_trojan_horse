import random

def welcome_message():
    print('Welcome to "Guess a Number!"')

def choose_difficulty():
    print('\nChoose difficulty:')
    print('[0] Easy')
    print('[1] Medium')
    print('[2] Hard')
    print('[3] Legend')
    try:
        choice = int(input('Your choice: '))
        assert(choice >= 0 or choice <= 3)
        return choice
    except:
        print('Please choose typing 1, 2 or 3.')
        return choose_difficulty()

def get_max_tries(difficulty):
    max_tries = 50 - (difficulty * 10)
    if difficulty == 3:
        max_tries = 1
    return max_tries


def game():
    welcome_message()
    max_tries = get_max_tries(choose_difficulty())
    number = random.randint(0, 100)
    tries = 0
    previous_numbers = []
    done = False

    print('Enter a guess between 0 and 100')
    while not done:
        tries += 1

        if tries >= max_tries:
            print('You lost!')
            done = True
            break

        guess = int(input(f'{tries}/{max_tries}: {previous_numbers} > '))

        if guess == number:
            done = True
            print('You won!')
        else:
            previous_numbers.append(guess)
            if guess > number:
                print('hint: the actual number is smaller')
            else:
                print('hint: the actual number is larger')

    print(f'You got it after {tries} tries!')