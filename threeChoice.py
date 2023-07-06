import random

user_score = 0
computer_score = 0
options = ['rock','paper','scissors']

while True:
    user_input = input('Type Rock/Paper/Scissors or Q to quit. ').lower()
    if user_input == 'q':
        break
    if user_input not in options:
        continue

    random_number = random.randint(0,2)    
    #rock is 0, paper is 1 and scissors is 2
    computer_guess = options[random_number]
    print('Computer picked',computer_guess + '.')

    if user_input == 'rock'and computer_guess == 'scissors':
        print('You win!')
        user_score += 1
        
    elif user_input == 'paper'and computer_guess == 'rock':
        print('You win!')
        user_score += 1
        
    elif user_input == 'scissors'and computer_guess == 'paper':
        print('You win!')
        user_score += 1

    elif user_input == computer_guess:
        print('It is a tie!')
        
    else:
        print('You lost!')
        computer_score += 1
           
print('You won',user_score,'times.')
print('The computer won',computer_score,'times.')
print('Goodbye!')