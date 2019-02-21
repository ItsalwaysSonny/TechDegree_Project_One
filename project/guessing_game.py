import random

min_number = 1
max_number = 20

random_number = random.randint(min_number, max_number)
# found use of random function via https://www.pythonforbeginners.com/random/how-to-use-the-random-module-in-python
guesses = []

def start_game():
    print("""
    Welcome to Sonny's Spectacular Number Guessing Game!!!
    >>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    How to play: Guess a number between 1 and 20. Don't worry if you get the number incorrect, Sonny will be there to help you along the way. Good Luck!
""")
    
    guesses = 0
    while True:
            
        try:
            guess = int(input("\nChoose a number between 1 and 20\n*  "))
            if guess < min_number or guess > max_number:
                raise ValueError("Please enter a number within the range of 1 through 20")
        except ValueError as err:
            print("PLease try again!")
            print(err)
            continue
        else:    
            guesses += 1
            if guess == random_number:
                print("Sonny thinks you've found the right number!! It took you {} guesses to get the right number".format(guesses))
                print("Thanks for playing :)")
                break
                
            elif guess < random_number:
                    print("Sonny thinks your number is a bit cold, try something higher!")
                    continue 
            elif guess > random_number:
                    print("Sonny thinks your number is a bit hot, try something lower!")
                    continue 
    return guesses

  
        

if __name__ == '__main__':
    start_game()
