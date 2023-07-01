import random #package for random numbers

top_range = input('Type a number: ') #getting the max. no. to guess

if top_range.isdigit(): #checking if integer
    top_range = int(top_range)

    if top_range <= 0:
        print('Please enter a number that is greater than 0.')
        quit()
else:
    print('Please enter a number next time.')
    quit()

random_number = random.randint(0, top_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input('Make a guess: ')

    if user_guess.isdigit(): #checking if integer
        user_guess = int(user_guess)
    else:
        print('Please enter a number next time.')
        continue

    if user_guess == random_number: #checking if the guess matches
        print('Yaay! You got it!')
        break

    elif user_guess > random_number:
        print('You guessed it above the number.')
    else:
        print('You guesses it below the number.')    
                     
print('You got it in',guesses,'guesses')