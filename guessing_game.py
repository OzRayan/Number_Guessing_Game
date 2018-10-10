import random
import os

range_of_numbers = tuple()


def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')


def game(guess_count):
    random_number = random.randrange(1, 11)
    guess_count.clear()
    while True:
        try:
            guess = int(input('Enter a number between 1 and 10:'))
            if guess < 1 or guess > 10:
                clear()
                print('Your number is not in the range of 1 and 10!')
            elif guess < random_number:
                clear()
                print('Your number is lower then my number')
                guess_count.append(guess)
            elif guess > random_number:
                clear()
                print('Your number is higher then my number')
                guess_count.append(guess)
            else:
                clear()
                print("Congratulation! You guessed my number, "
                      + str(random_number))
                guess_count.append(guess)
                break
        except ValueError:
            print('Please enter a number!')


def start_game():
    option = None
    guess_count = []
    print('Welcome to Number Guessing Game\n'
          'Lower score wins. Good luck!')
    while option != 'n':
        game(guess_count)
        score = len(guess_count)
        print('Your score is {}'.format(score))
        option = input('Would you like to continue? [y]es [N]o >').lower()
        clear()


if __name__ == '__main__':
    start_game()
