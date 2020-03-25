from random import randint

PLAYER_1 = 0
PLAYER_1_CARDS = randint(2,11)
PLAYER_2_CARDS = randint(2,11)
PLAYER_3_CARDS = randint(2,11)
MAX_CARD = PLAYER_1_CARDS + PLAYER_2_CARDS

print('Welcome to the game, please take a card ')
print('You  have points - ' + str(PLAYER_1_CARDS))
print('You  have points - ' + str(PLAYER_2_CARDS))
print('This is all your points - ' + str(MAX_CARD))
print('')

if MAX_CARD < 21:
    PLAYER_1 = 1

while PLAYER_1:
    step = input('You are take a new card - ?' '[y/n]')

    if step == 'y':
        PLAYER_3_CARDS = randint(2, 11)
        MAX_CARD += PLAYER_3_CARDS
        print('So, you  have point - ' + str(MAX_CARD))

    if step == 'n':
        print('So, you  have point - ' + str(MAX_CARD))
        
        if MAX_CARD <= 21:
            print('You are win!')
        elif MAX_CARD > 21:
            print('You lost. Try again')
        break

    if MAX_CARD == 21:
        print ('You are win!')
        break

    if MAX_CARD >= 15 and MAX_CARD <= 21:
        print('You are win! You  have point - ' + str(MAX_CARD))
        break

    elif MAX_CARD > 21:  
        print('You lost. Try again =(')
        
    elif PLAYER_1_CARDS == 11 and PLAYER_2_CARDS == 11:
        print('Black JACK!, You are win!')

    if  PLAYER_1 > MAX_CARD or MAX_CARD > 21:
        
        if MAX_CARD > 21:
            print('Sorry, you have point - ' + str(MAX_CARD))
            
        else:
            print('Game is closed!See you soon!')
        break
