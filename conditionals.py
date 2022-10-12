# Conditional
# Method evaluate data
# if then else

import random
#ask the user to select the upper bound
invalid_upper_bound = True # boolean True or False

while invalid_upper_bound:
    upper_bound = input("What is the upper bound? ")
    #check if upper bound is valid returns -> string
    if upper_bound.isdigit():
        upper_bound = int(upper_bound)
        invalid_upper_bound = False
    else:
        print('That is not a valid input')

# generate a random integer starting at 1 and going to upper_bound
random_number = random.randint(1, upper_bound)
print(random_number)

user_guess = 0
number_of_guesses = 1
#start and loop here
while user_guess != random_number:
    #ask the user to guess
    user_guess = input("Type a number between 1 and " + str(upper_bound) + ": ")
    
    #check if guess is a digit
    if user_guess.isdigit():
        user_guess = int(user_guess)

    # check if user guess = random number
    if user_guess == random_number:
        print("You win")
        # exit the loop
    # user guess is not equal to random number
    else:
        print("You lose")
        number_of_guesses += 1

print("Game Over you took " + str(number_of_guesses) + " guesses")   