import random
import sys
import math
def getNewBoard():
    board = []
    for x in range(60):
        board.append([])
        for y in range(15):
            if random.randint(0,1) == 0:
                board[x].append("~")
            else:
                board[x].append('`')
    return board
def drawBoard(board):
    tensDigitsLine = '    '
    for i in range(1,6):
        tensDigitsLine += (' '*9) + str(i)

    print(tensDigitsLine)
    print('   ' + ('0123456789'*6))
    print()

    for row in range(15):
        if row < 10:
            extraSpace = ' '
        else:
            extraSpace = ''

        boardRow = ''
        for column in range(60):
            boardRow += board[column][row]

        print(f'{extraSpace}{row} {boardRow} {row}')

    print()
    print("   " + ('0123456789' * 6))
    print(tensDigitsLine)
def getRandomChests(numChests):
    chests = []
    while len(chests) < numChests:
        newChest = [random.randint(0,59), random.randint(0,14)]
        if newChest not in chests:
            chests.append(newChest)
    return chests
def isOnBoard(x, y):
    return x >= 0 and x <= 59 and y >=0 and y <= 14
def makeMove(board, chests, x, y):
    smallestDistance = 100
    for cx, cy in chests:
        distance = math.sqrt((cx - x) * (cx - x) + (cy-y) * (cy-y))

        if distance < smallestDistance: 
            smallestDistance = distance

    smallestDistance = round(smallestDistance)

    if smallestDistance == 0:
        theChests.remove([x,y])
        board[x][y] = "C"
        return "You have found a sunken treasure chest!"
    
    else:
        if smallestDistance < 10:
            board[x][y] = str(smallestDistance)
            return f"Treasure detacted at a distance of {smallestDistance} from the sonar device."
        else:
            board[x][y] = 'X'
            return "Sonar did not detect anything. All treasure chests out of range."       
def enterPlayerMove(previousMoves):
    print("Where do you want to drop the next sonar device? (0-59 0-14) (or type quit)")
    while True:
        move = input().lower()
        if move == 'quit':
            print('Thanks for playing')
            sys.exit()
        
        move = move.split()
        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and isOnBoard(int(move[0]), int(move[1])):
            if [int(move[0]),int(move[1])] in previousMoves:
                print("You already moved there.")
                continue
            return [int(move[0]),int(move[1])]
        
        print('Enter a number from 0 to 59, a space, then a number from 0-14')
def showInstructios():
    print("""Instructions:
    You are the captain of the Simon, a treasure-hunting ship. Your current mission
    is to use sonar devices to find three sunken treasure chests at the bottom of
    the ocean. But you only have cheap sonar that finds distance, not direction.
    
    Enter the coordinates to drop a sonar device. The ocean map will be marked with 
    how far away the nearest chest is, or an X if it is beyond the sonar device's 
    range. For example the C marks are where chests are. The sonar device shows a 
    3 because the closest chest is 3 spaces away.
    
                  1         2         3
        012345678901234567890123456789012
        
      0 ~~``~~`~~``~~`~~~``~~``~~`~`~`~`~` 0
      1 ~~``~~`~~``~~`~~~``~~``~~`~`~`~`~` 1
      2 ~~`C~~3~~``~~`~~~C`~~``~~`~`~`~`~` 2
      3 ~~``~~`~~``~~`~~~``~~``~~`~`~`~`~` 3
      4 ~~``~~`~~``~~`~~~C`~~``~~`~`~`~`~` 4
       
        012345678901234567890123456789012 
                  1         2         3    
                  
    (In the real game, the chests are not visible in the ocean.)
        
    Press enter to continue...""")
    input()

    print('''When you drop a sonar device directly on a chest, you retrieve it and the other
    sonar devices update to show how far away the next nearest chest is. The chests
    are beyond the range of the sonar device on the left, so it shows an X.
    
                  1         2         3
        012345678901234567890123456789012
        
      0 ~~``~~`~~``~~`~~~``~~``~~`~`~`~`~` 0
      1 ~~``~~`~~``~~`~~~``~~``~~`~`~`~`~` 1
      2 ~~`X~~7~~``~~`~~~C`~~``~~`~`~`~`~` 2
      3 ~~``~~`~~``~~`~~~``~~``~~`~`~`~`~` 3
      4 ~~``~~`~~``~~`~~~C`~~``~~`~`~`~`~` 4
       
        012345678901234567890123456789012 
                  1         2         3    
    The treasure chests don't move around. Sonar devices can detect treasure chests
    up to a distance of 9 spaces. Try to collect all 3 chests before running out of 
    sonar devices. Good luck!
    Press enter to continue...''')
    input()
print('S O N A R')
print()
print("Would you like to view the instructions? (yes/no)")
if input().lower().startswith('y'):
    showInstructios()

while True:
    sonarDevices = 20
    theBoard = getNewBoard()
    theChests = getRandomChests(3)
    drawBoard(theBoard)
    previousMoves = []

    while sonarDevices > 0:
        print(f'You have {sonarDevices} sonar device(s) left. {len(theChests)} treasure chest(s) remaining.')
        x, y = enterPlayerMove(previousMoves)
        previousMoves.append([x,y])

        moveResult = makeMove(theBoard, theChests, x ,y)
        if moveResult == False:
            continue
        else:
            if moveResult == 'You have found a suken treasure chest!':
                for x,y in previousMoves:
                    makeMove(theBoard, theChests, x , y)
            drawBoard(theBoard)
            print(moveResult)

        if len(theChests) == 0:
            print('You have found all the sunken treasure chests! Congratulations and good game!')
            break;
        sonarDevices -=1
    if sonarDevices == 0:
        print("We've run out of sonar devices! Now we have to turn the ship around and head")
        print('for home with treasure sill out there! Game over.')
        print('    The remaining chests were here:')
        for x, y in theChests:
            print(f'   {x}, {y}')
        print('Do you want to play agian? (yes or no)')
        if not input().lower().startswith('y'):
            sys.exit()

