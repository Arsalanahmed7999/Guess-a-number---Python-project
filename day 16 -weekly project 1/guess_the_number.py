import random
actualNum = (random.randint(1, 10)) #random number 1-10
print('Guess a number between 1-10, Create your highscore')
print('You have only 6 attempts to make a guess')
attempts = 0
while True:
    attempts+=1
    guess = int(input('Make a guess: \n'))
    if attempts>5:
        break
    if guess>actualNum:
        print(f'{guess} is greater than the actual number')
    elif guess<actualNum:
        print(f'{guess} is less than the actual number')
    else:
        print(f'{guess} is equal to actual number')
        break
    
if(attempts>5):
    print('You exceeded the attempts limit count')
else:
    print(f'You took {attempts} attempts to make a correct guess')

        
    



    
