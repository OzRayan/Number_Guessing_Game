# Header prompt, welcome

# Loop till guess correct

# Bigger smaller prompt

# number range for guesses

import random



header_prompt = 'Welcome to Number Guessing Game'
guess = None
guess_count = []
range_of_numbers = tuple()


def game():
    random_number = random.randrange(1, 11)
    guess_count.clear()
    prompt = 'Your number is {} then my number'
    choice = ('lower', 'higher')
    while True:
        try:
            guess = int(input('Enter a number between 1 an 10:'))
            if guess < random_number:
                print(prompt.format(choice[0]))
                guess_count.append(guess)
            elif guess > random_number:
                print(prompt.format(choice[1]))
                guess_count.append(guess)
            else:
                print("Congratulation! You guessed the number")
                break
        except ValueError:
            print('Please enter a number')


def main():
    option = None
    print(header_prompt)

    while option != 'n':
        game()
        score = len(guess_count)
        print('Your score is {}'.format(score))
        option = input('Would you like to continue? [y]es [N]o >').lower()


if __name__ == '__main__':
    main()