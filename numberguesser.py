def dumberguesser():
    guess = 1
    responses = {'y' : True, 'n' : False}

    input("Think of a number between 1 and 100, inclusive, and hit ENTER. I'm going to try to guess it.")
    while True:
        response = input(f'Is it {guess} [Y/n]?').lower() or 'y' # Defaults to y (yes, you have to type 'n' each time it's wrong)
        correct = responses.get(response[0], True) # If not y or n, default to True (y)
        if correct:
            print(f'I knew it was {guess}!')
            break
        elif guess == 51: # Yes, this guesser gives up halfway
            print("I give up")
            break
        guess += 1

if __name__ == "__main__":
    dumberguesser()