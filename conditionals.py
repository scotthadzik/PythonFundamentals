# Conditional
# Method evaluate data
# if then else

import random

high_range = 100
middle_number = int(high_range/2)
my_guess = middle_number
number_guesses = 0
highOrLow = "lower"
output = "{} is {} than {}"

my_random_number = random.randint(1, high_range)

print(my_random_number)
print(my_guess)

#evaluate the radom number and compare it to middle number
if my_guess < my_random_number:
    highOrLow = "lower"
    
if my_guess > my_random_number :
    highOrLow = "higher"

print(output.format(my_guess, highOrLow, my_random_number))
