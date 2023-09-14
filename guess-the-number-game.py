import random
lives = 5
upper_number = int(input('Enter your upper bound: '))

lower_number = int(input('Enter your lower bound: '))
# boundaries for the number range

number = random.randint(int(lower_number) , int(upper_number))
# lets the computer choose the number


def random_number_game(lives):
        guess = input('Take a guess: ')
        if int(guess) > number:
            print('Too High!')
            lives -= 1
            print(f'you have', lives, 'lives left')
        if int(guess) < number:
            print('Too Low!')
            lives -= 1
            print(f'you have', lives, 'lives left')

        elif int(guess) == number:
                print('You Won!')
                breakpoint
        if lives == 0:
            print('You lost too many lies, try again!')
            breakpoint

        while lives > 0:
            random_number_game(lives)
        while lives == 0:
            break

        random_number_game(lives)
# start of the game
print('Here are the rules: \
      1) You have 5 tries/lives) to guess the correct number \
      2) I will tell you if you are too high, too low, or if you have guessed the number correctly \
      3) Have Fun cause I spent too long coding this :(')

random_number_game(lives)
