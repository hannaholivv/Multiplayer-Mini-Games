# Connect Four
def createBoard():
    global r, c
    r, c = 6, 7
    if 'n' == input('Standard game? (y/n): '):
        r, c = int(input('r? (2 - 20): ')), int(input('c? (2 - 20): '))
    return [['·'] * c for i in range(r)]

def printBoard(board):
    r, c = len(board), len(board[0])
    spaces = 1
    if r>9 or c>9: spaces = 2 #bigBoard
    x = ''
    for row in range(r-1,-1, -1):
        x += f'{row:>{spaces}}'
        ss = ' '
        if spaces==2: ss = '  '
        for col in range(c):
            x += ss+board[row][col]
        x += ' \n'
    x += ' ' + ' '*spaces
    for col in range(c): x += f'{col:>{spaces}}'+' '
    print(x)

def makeMove(board, player, col):
    r = len(board)
    for row in range(r):
        if board[row][col]!='·' and board[row+1][col]=='·':
            board[row+1][col] = player
            break
        elif board[row][col]=='·':
            board[row][col] = player
            break

def winning(player):
    for row in board:
        count = 0
        for i in range(len(row)):
            if row[i] == player: count += 1
            elif row[i] != player: count = 0
            if count == 4: return True

    for col in range(c): # 0 1 2 3 4 5
        count = 0
        for row in range(r): # 0 1 2 3 
            if board[row][col] == player: count += 1
            elif board[row][col] != player: count = 0
            if count == 4: return True

    for row in range(r-3):
        for col in range(c-3):  
            if board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][col + 2] == player and board[row + 3][col + 3] == player: return True 
    
    for row in range(r-3):
        for col in range(c):
            if board[row][col] == player and board[row + 1][col - 1] == player and board[row + 2][col - 2] == player and board[row + 3][col - 3] == player: return True 

board = createBoard()
printBoard(board)
player = 'X'
step = 0
while True:
    move = input( 'player'+player+' (col #): ')
    if move == 'e': break
    if board[r-1][int(move)] != "·":
        printBoard(board)
        continue
    makeMove(board, player, int(move))
    printBoard(board)
    step += 1
    if winning(player) == True: 
        print(f'Player {player} has won!')
        break
    if step == r * c:
        print('Draw!')
        break
    if player == 'X': player = 'O'
    else: player = 'X'
print('bye')
