import re
from utility import getInputText

max = {'red': 12, 'green': 13, 'blue': 14}
def getGameID(line):
    gameID = re.search('[0-9][0-9]?[0-9]?', line).group()
    return gameID

def isGamePossible(game):
    # Is each individual hand possible?
    for hand in game:
        colors = hand.split(', ')
        if not isHandPossible(colors):
            return False
    return True


def isHandPossible(colors):
    # Go through each color and see if it is possible.
    for color in colors:
        amt = color.split(' ')[0]
        color_name = color.split(' ')[1]

        # Check against the max.
        if int(amt) > max[color_name]:
            return False
    return True

# Grab the text.
txt = getInputText('input.txt')
total = 0

# Get down to business.
for line in txt:
    # Get the hands, apart from the game ID.
    game = line.split(': ')[1].split('; ')

    # If the hand is possible, get the game ID.
    if isGamePossible(game):
        gameID = getGameID(line)
        total += int(gameID)

print(total)