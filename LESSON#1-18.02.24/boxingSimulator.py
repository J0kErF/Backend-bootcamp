import random


moves =['Jab','Cross','Lead Hook','Rear Hook','Lead Upperut','Rear Uppercut']

def boxingSimulator():
    print('Welcome to the Boxing Simulator')
    print('You will be fighting against a computer opponent')
    print('The fight will last for 3 rounds')
    print('You will be able to choose from the following moves:')
    for i in range(len(moves)):
        print(i+1,moves[i])
    print('Good luck!')

    # Start the fight
    round = 1
    while round <= 3:
        print('Round', round)
        # Player move
        playerMove = input('Enter your move: ')
        playerMove = int(playerMove) - 1
        # Computer move
        computerMove = random.randint(0,5)
        print('The computer used', computerMove)
        print('You used', playerMove)
        # Determine the winner of the round
        if playerMove == computerMove:
            print('It is a tie!')
        if playerMove > computerMove:
            if playerMove - computerMove != 5:
                print('You win the round!')
        else:
            if computerMove - playerMove == 5:
                print('You win the round!')
            else:
                print('You lose the round!')
        
        round += 1
    print('The fight is over!')
boxingSimulator()