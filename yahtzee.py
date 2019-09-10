import pygame
import random
import time

# Methods will all be initialized here.
def rollDice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    die3 = random.randint(1, 6)
    die4 = random.randint(1, 6)
    die5 = random.randint(1, 6)

    list = [die1, die2, die3, die4, die5]
    return list

def reroll(currSet, indicesToKeep):
    for dice in range(0, 5):
        if not(dice in indicesToKeep):
            currSet[dice] = random.randint(1, 6)
    return currSet

def showDice(array):
    print("{} {} {} {} {}".format(array[0], array[1], array[2], array[3], array[4]))

# Define the player class.
class Player:
    name = ""
    score = 0               # overall score
    bonus = False           # calculate this at the end of the game
    isPlaying = False       # is it their turn?
    currRolls = 0           # can only take up to 3 turns
    iterations = 0          # how many fill-ins did they have?

    # if the combined score of this section is over 63, the bonus becomes True
    aces = 0
    playedAces = False
    twos = 0
    playedTwos = False
    threes = 0
    playedThrees = False
    fours = 0
    playedFours = False
    fives = 0
    playedFives = False
    sixes = 0
    playedSixes = False

    # when you perfect the top section, fill in the other sections

# game initialization phase
numPlayers = 2
player1 = Player()
player2 = Player()
print("Player 1, what is your name?")
player1.name = input()
print("Player 2, what is your name?")
player2.name = input()

print("Alright, let us commence!")
time.sleep(2)
print("Time for the coin flip to see who's going to play first!")
time.sleep(2)
print("Who is it? Let's find out...")
# Commencement sound.
pygame.mixer.init()         # must be called before pygame.init() if you want to play sound w/o opening a window
pygame.mixer.music.load('drumroll.wav')
pygame.mixer.music.play()
time.sleep(7)

startNum = random.randint(1, 2)
if(startNum == 1):
    player1.isPlaying = True
    print("{} goes first!".format(player1.name))
else:
    player2.isPlaying = True
    print("{} goes first!".format(player2.name))

if player1.isPlaying:
    print("{}, take it away!".format(player1.name))
else:
    print("{}, take it away!".format(player2.name))

time.sleep(5)

# assume the dice haven't been partially altered yet
diceAltered = False

# time to jump into the game
gameLoop = True
while gameLoop:

    # when the game is over, break the loop
    if(player1.iterations == 6 and player2.iterations == 6):
        break

    # should be roughly the same as when player 2 is playing
    while player1.isPlaying and player1.iterations < 6:
        if player1.currRolls == 4:
            player1.currRolls = 0       # set the number of rolls back to zero
            player1.iterations += 1
            player1.isPlaying = False
            player2.isPlaying = True
            diceAltered = False         # nothing was showing up for the second player
            break

        print()
        print("Your current score is: {}".format(player1.score))
        if(diceAltered == False):
            currRoll = rollDice()
            showDice(currRoll)
            player1.currRolls += 1
        else:
            showDice(newRoll)

        actionNotTaken = True
        # while they didn't choose what to play yet
        while actionNotTaken:
            print()
            print("Your scorecard:")
            print("Aces: ", player1.aces)
            print("Twos: ", player1.twos)
            print("Threes: ", player1.threes)
            print("Fours: ", player1.fours)
            print("Fives: ", player1.fives)
            print("Sixes: ", player1.sixes)
            print()
            print("What do you want to play, {}?".format(player1.name))
            action = input()
            # have to make sure they didn't play that category before
            if(action == "again" and player1.currRolls < 3):
                print("Alright, let's roll again!")
                print("Do you want to keep any dice?")
                response = input()
                if(response == "yes"):
                    print("How many dice do you want to keep?")
                    number = input()
                    number = int(number)
                    print("Which dice do you want to keep?")
                    keepers = []
                    for num in range(0, number):
                        keeper = input()
                        keeper = int(keeper)
                        keepers.append(keeper)
                    newRoll = reroll(currRoll, keepers)
                    # showDice(newRoll)
                    player1.currRolls += 1
                    diceAltered = True
                if(response == "no"):
                    diceAltered = False
                actionNotTaken = False
            if(action == "aces" and player1.playedAces == False):
                for die in range(0, 5):
                    if currRoll[die] == 1:
                        player1.aces += 1
                        player1.score += 1
                player1.playedAces = True
                player1.currRolls = 0      # set the number of rolls back to zero
                player1.iterations += 1
                player1.isPlaying = False
                player2.isPlaying = True
                actionNotTaken = False
                diceAltered = False        # prevent the inheritance problem
            if(action == "twos" and player1.playedTwos == False):
                for die in range(0, 5):
                    if currRoll[die] == 2:
                        player1.twos += 2
                        player1.score += 2
                player1.playedTwos = True
                player1.currRolls = 0  # set the number of rolls back to zero
                player1.iterations += 1
                player1.isPlaying = False
                player2.isPlaying = True
                actionNotTaken = False
                diceAltered = False  # prevent the inheritance problem
            if(action == "threes" and player1.playedThrees == False):
                for die in range(0, 5):
                    if currRoll[die] == 3:
                        player1.threes += 3
                        player1.score += 3
                player1.playedThrees = True
                player1.currRolls = 0  # set the number of rolls back to zero
                player1.iterations += 1
                player1.isPlaying = False
                player2.isPlaying = True
                actionNotTaken = False
                diceAltered = False  # prevent the inheritance problem
            if(action == "fours" and player1.playedFours == False):
                for die in range(0, 5):
                    if currRoll[die] == 4:
                        player1.fours += 4
                        player1.score += 4
                player1.playedFours = True
                player1.currRolls = 0  # set the number of rolls back to zero
                player1.iterations += 1
                player1.isPlaying = False
                player2.isPlaying = True
                actionNotTaken = False
                diceAltered = False  # prevent the inheritance problem
            if(action == "fives" and player1.playedFives == False):
                for die in range(0, 5):
                    if currRoll[die] == 5:
                        player1.fives += 5
                        player1.score += 5
                player1.playedFives = True
                player1.currRolls = 0  # set the number of rolls back to zero
                player1.iterations += 1
                player1.isPlaying = False
                player2.isPlaying = True
                actionNotTaken = False
                diceAltered = False  # prevent the inheritance problem
            if(action == "sixes" and player1.playedSixes == False):
                for die in range(0, 5):
                    if currRoll[die] == 6:
                        player1.sixes += 6
                        player1.score += 6
                player1.playedSixes = True
                player1.currRolls = 0  # set the number of rolls back to zero
                player1.iterations += 1
                player1.isPlaying = False
                player2.isPlaying = True
                actionNotTaken = False
                diceAltered = False  # prevent the inheritance problem

    while player2.isPlaying and player2.iterations < 6:
        if player2.currRolls == 4:
            player2.currRolls = 0  # set the number of rolls back to zero
            player2.iterations += 1
            player2.isPlaying = False
            player1.isPlaying = True
            diceAltered = False
            break

        print()
        print("Your current score is: {}".format(player2.score))
        if(diceAltered == False):
            currRoll = rollDice()
            showDice(currRoll)
            player2.currRolls += 1
        else:
            showDice(newRoll)

        actionNotTaken = True
        # while they didn't choose what to play yet
        while actionNotTaken:
            print()
            print("Your scorecard:")
            print("Aces: ", player2.aces)
            print("Twos: ", player2.twos)
            print("Threes: ", player2.threes)
            print("Fours: ", player2.fours)
            print("Fives: ", player2.fives)
            print("Sixes: ", player2.sixes)
            print()
            print("What do you want to play, {}?".format(player2.name))
            action = input()
            # have to make sure they didn't play that category before
            if (action == "again" and player2.currRolls < 3):
                print("Alright, let's roll again!")
                print("Do you want to keep any dice?")
                response = input()
                if(response == "yes"):
                    print("How many dice do you want to keep?")
                    number = input()
                    number = int(number)
                    print("Which dice do you want to keep?")
                    keepers = []
                    for num in range(0, number):
                        keeper = input()
                        keeper = int(keeper)
                        keepers.append(keeper)
                    newRoll = reroll(currRoll, keepers)
                    # showDice(newRoll)
                    player2.currRolls += 1
                    diceAltered = True
                if(response == "no"):
                    diceAltered = False
                actionNotTaken = False
            if (action == "aces" and player2.playedAces == False):
                for die in range(0, 5):
                    if currRoll[die] == 1:
                        player2.aces += 1
                        player2.score += 1
                player2.playedAces = True
                player2.currRolls = 0  # set the number of rolls back to zero
                player2.iterations += 1
                player2.isPlaying = False
                player1.isPlaying = True
                actionNotTaken = False
                diceAltered = False  # prevent the inheritance problem
            if (action == "twos" and player2.playedTwos == False):
                for die in range(0, 5):
                    if currRoll[die] == 2:
                        player2.twos += 2
                        player2.score += 2
                player2.playedTwos = True
                player2.currRolls = 0  # set the number of rolls back to zero
                player2.iterations += 1
                player2.isPlaying = False
                player1.isPlaying = True
                actionNotTaken = False
                diceAltered = False  # prevent the inheritance problem
            if (action == "threes" and player2.playedThrees == False):
                for die in range(0, 5):
                    if currRoll[die] == 3:
                        player2.threes += 3
                        player2.score += 3
                player2.playedThrees = True
                player2.currRolls = 0  # set the number of rolls back to zero
                player2.iterations += 1
                player2.isPlaying = False
                player1.isPlaying = True
                actionNotTaken = False
                diceAltered = False  # prevent the inheritance problem
            if (action == "fours" and player2.playedFours == False):
                for die in range(0, 5):
                    if currRoll[die] == 4:
                        player2.fours += 4
                        player2.score += 4
                player2.playedFours = True
                player2.currRolls = 0  # set the number of rolls back to zero
                player2.iterations += 1
                player2.isPlaying = False
                player1.isPlaying = True
                actionNotTaken = False
                diceAltered = False  # prevent the inheritance problem
            if (action == "fives" and player2.playedFives == False):
                for die in range(0, 5):
                    if currRoll[die] == 5:
                        player2.fives += 5
                        player2.score += 5
                player2.playedFives = True
                player2.currRolls = 0  # set the number of rolls back to zero
                player2.iterations += 1
                player2.isPlaying = False
                player1.isPlaying = True
                actionNotTaken = False
                diceAltered = False  # prevent the inheritance problem
            if (action == "sixes" and player2.playedSixes == False):
                for die in range(0, 5):
                    if currRoll[die] == 6:
                        player2.sixes += 6
                        player2.score += 6
                player2.playedSixes = True
                player2.currRolls = 0  # set the number of rolls back to zero
                player2.iterations += 1
                player2.isPlaying = False
                player1.isPlaying = True
                actionNotTaken = False
                diceAltered = False  # prevent the inheritance problem

# calculate the bonus points
if(player1.score >= 63):
    print("{} got the bonus!".format(player1.name))
    player1.score += 35
else:
    print("{} didn't get the bonus because they sucked!".format(player1.name))
if(player2.score >= 63):
    print("{} got the bonus!".format(player2.name))
    player2.score += 35
else:
    print("{} didn't get the bonus because they sucked!".format(player2.name))

print()
print("Now that the game is over, the winner is...")
print()
time.sleep(5)

if(player1.score > player2.score):
    print("{}!".format(player1.name))
elif(player2.score > player1.score):
    print("{}!".format(player2.name))
else:
    print("Against all odds, it's a tie game!")

print()
print("This was the final score:")
print("{} ended up with {} points.".format(player1.name, player1.score))
print("{} ended up with {} points.".format(player2.name, player2.score))