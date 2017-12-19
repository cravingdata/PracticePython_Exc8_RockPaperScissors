#UNFINISHED.  TRY TO GET PLAYER TO SPELL CORRECTLY AND CORRECT ANY MISPELLING.



stoploop = True

index = 0
while stoploop:
    player1 = raw_input("Player 1, choose Rock [R], Paper [P], or Scissors [S]: ")
    if player1 != 'rock' and player1 != 'paper' and player1 != 'scissors':
        print "Try retyping again."
        print player1
    player2 = raw_input("Player 2, choose Rock, Paper, or Scissors: ")
    if player2 != 'rock' and player2 != 'paper' and player2 != 'scissors':
        print "Try retyping again."
        print player2
    if player1 == player2:
        print "This is a draw."
    elif player1 == "rock":
        if player1 == "rock":
            print "Player 1 wins!"
        elif player2 == "rock":
            print "Player 2 wins!"
    elif player1 == "paper":
        if player1 == "paper" and player2 == "rock":
            print "Player 1 wins!"
        else:
            print "Player 2 wins!"
    elif player1 == "scissors":
        if player1 == "scissors" and player2 == "rock":
            print "Player 2 wins!"
        else:
            print "Player 1 wins!"
        #player1 = raw_input("Player 1, choose Rock, Paper, or Scissors: ")
        #player2 = raw_input("Player 2, choose Rock, Paper, or Scissors: ")
    print

    replay = raw_input("Do you want to play again? Enter Y for 'yes' and N for 'no': ")
    if replay == 'Y':
        player1 = raw_input("Player 1, choose Rock, Paper, or Scissors: ")
        player2 = raw_input("Player 2, choose Rock, Paper, or Scissors: ")
    else:
        stoploop = False



#print raw_input("Press Y if you want to play again and N if you want to end game: ")

#for option in play_game:
