import random, time

CPUboard2 = [[1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0]]

CPUboard1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

playerBoard1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

playerBoard2 = [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 0, 0, 0, 0]]

coords = {'A1': [0, 0], 'B1': [0, 1], 'C1': [0,2], 'D1': [0, 3], 'E1': [0, 4], 'F1': [0, 5], 'G1': [0, 6], 'H1': [0, 7], 'I1': [0, 8],
          'J1': [0, 9], 'A2': [1, 0], 'B2': [1, 1], 'C2': [1, 2], 'D2': [1, 3], 'E2': [1, 4], 'F2': [1, 5], 'G2': [1, 6], 'H2': [1, 7],
          'I2': [1, 8], 'J2': [1, 9], 'A3': [2, 0], 'B3': [2, 1], 'C3': [2, 2], 'D3': [2, 3], 'E3': [2, 4], 'F3': [2, 5], 'G3': [2, 6],
          'H3': [2, 7], 'I3': [2, 8], 'J3': [2, 9], 'A4': [3, 0], 'B4': [3, 1], 'C4': [3, 2], 'D4': [3, 3], 'E4': [3, 4], 'F4': [3, 5],
          'G4': [3, 6], 'H4': [3, 7], 'I4': [3, 8], 'J4': [3, 9], 'A5': [4, 0], 'B5': [4, 1], 'C5': [4, 2], 'D5': [4, 3], 'E5': [4, 4],
          'F5': [4, 5], 'G5': [4, 6], 'H5': [4, 7], 'I5': [4, 8], 'J5': [4, 9], 'A6': [5, 0], 'B6': [5, 1], 'C6': [5, 2], 'D6': [5, 3],
          'E6': [5, 4], 'F6': [5, 5], 'G6': [5, 6], 'H6': [5, 7], 'I6': [5, 8], 'J6': [5, 9], 'A7': [6, 0], 'B7': [6, 1], 'C7': [6, 2],
          'D7': [6, 3], 'E7': [6, 4], 'F7': [6, 5], 'G7': [6, 6], 'H7': [6, 7], 'I7': [6, 8], 'J7': [6, 9], 'A8': [7, 0], 'B8': [7, 1],
          'C8': [7, 2], 'D8': [7, 3], 'E8': [7, 4], 'F8': [7, 5], 'G8': [7, 6], 'H8': [7, 7], 'I8': [7, 8], 'J8': [7, 9], 'A9': [8, 0],
          'B9': [8, 1], 'C9': [8, 2], 'D9': [8, 3], 'E9': [8, 4], 'F9': [8, 5], 'G9': [8, 6], 'H9': [8, 7], 'I9': [8, 8], 'J9': [8, 9],
          'A10': [9, 0], 'B10': [9, 1], 'C10': [9, 2], 'D10': [9, 3], 'E10': [9, 4], 'F10': [9, 5], 'G10': [9, 6], 'H10': [9, 7],
          'I10': [9, 8], 'J10': [9, 9]}

def printBoard(board):
    count = 1
    print('  ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J')
    for y in range(10):
        for x in range(10):
            if x == 0:
                if count < 10:
                    print(' ' + str(count), end=' ')
                else:
                    print(count, end=' ')
                count += 1
            if x < 9:
                print(board[y][x], end=' ')
            else:
                print(board[y][x])

playerHitCount = 0
CPUhitCount = 0

print('''
=====================================

---------- BATTLESHIPS --------------

------- PLAYER VS COMPUTER ----------

=====================================
''')

while playerHitCount < 19 and CPUhitCount < 19:
    print("--- Player's turn ---")
    print()
    printBoard(playerBoard1)
    print()
    printBoard(playerBoard2)
    print()
    print('Enter a coordinate:')
    playerGuess = input().upper()
    if len(playerGuess) > 3 or playerGuess[0].isalpha() == False or playerGuess[1].isdigit() == False:
        print('Invalid input')
        continue

    #check for ship
    if CPUboard2[coords[playerGuess][0]][coords[playerGuess][1]] == 1:
        print('Hit!')
        print()
        playerBoard1[coords[playerGuess][0]][coords[playerGuess][1]] = 'x'
        playerHitCount += 1
        CPUboard2[coords[playerGuess][0]][coords[playerGuess][1]] = 'x'
    else:
        print('Miss!')
        print()
    if playerHitCount == 19:
        break

    print("--- Computer's turn ---")
    print()
    time.sleep(2)
    CPUguess, CPUcoords = random.choice(list(coords.items()))
    print(CPUguess)
    if playerBoard2[CPUcoords[0]][CPUcoords[1]] == 1:
        print('Hit!')
        print()
        CPUboard1[CPUcoords[0]][CPUcoords[1]] = 'x'
        CPUhitCount += 1
        playerBoard2[CPUcoords[0]][CPUcoords[1]] = 'x'
    else:
        print('Miss!')
        print()

if playerHitCount == 19:    
    print('You won!')
elif CPUhitCount == 19:
    print('You lost!')
































    
