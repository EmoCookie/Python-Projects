#Basic Quiz Game
print('Weclome to the Quiz Game!')

playing = input('Do you want to play? ') #Asking if user wants to play

if playing.lower() != 'yes': 
    quit()
print('Okay! Let\'s play')
score = 0

answer = input('What does UN stand for? ') #question 1
if answer.lower() == 'united nations':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('What does GPU stand for? ') #question 2
if answer.lower() == 'graphics processing unit':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('What does SDLC  stand  for? ') #question 3
if answer.lower() == 'software development lifecycle':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('What does RAM stand for? ') #question 4
if answer.lower() == 'random access memory':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print('You got ' + str(score) + ' questions correct!') #number of questions that were correct
print('You got ' + str((score / 4) * 100) + ' %.') #points