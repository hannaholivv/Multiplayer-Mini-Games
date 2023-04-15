# Tic Tac Toe
def board():
    global board, size
    size = int(input('Size--> '))
    board = []
    if size > 2 and size < 11:
        for i in range(size):
            lst = list(range(size*i,size*i+size)) 
            board.append(lst)

def printboard():
    for ii in board:
        for iii in ii[:-1]:
            print(str(iii).rjust(2), end = ' ')
        print(str(ii[-1]).rjust(2))

def playX():
    X= int(input('X--> '))
    board[X // size][X % size] = 'X'
    printboard()

def playO():
    O = int(input('O--> '))
    board[O // size][O % size] = 'O'
    printboard()

def winning():
    count = 0
    while count != size:
        playX()
        count =0
        for i in board:
            for ii in i: #cek row
                if ii == 'X':
                    count += 1
            if count == size:
                print('Winner: X')
                exit()
            count = 0
        
        for i in range(size): #cek column
            for ii in range(size):
                if board[ii][i] == 'X':
                    count += 1
            if count == size:
                print('Winner: X')
                exit()
            count = 0
        for i in range(size):
            if board[i][i] == 'X': #cek diagonal1
                count += 1
            if count == size:
                print('Winner: X')
                exit()
        count = 0
        for i in range(size - 1, -1, -1):
            if board[i][size-i-1] == 'X': #cek diagonal2
                count += 1
            if count == size:
                print('Winner: X')
                exit()
        tiecheck()
            
        playO()
        count = 0
        for i in board:
            for ii in i: #cek row
                if ii == 'O':
                    count += 1
            if count == size:
                print('Winner: O')
                exit()
            count = 0
        for i in range(size): #cek column
            for ii in range(size):
                if board[ii][i] == 'O':
                    count += 1
            if count == size:
                print('Winner: O')
                exit()
            count = 0
        for i in range(size):
            if board[i][i] == 'O': #cek diagonal1
                count += 1
            if count == size:
                print('Winner: O')
                exit()
        count = 0    
        for i in range(size - 1, -1, -1):
            if board[i][size-i-1] == 'O': #cek diagonal2
                count += 1
            if count == size:
                print('Winner: O')
                exit()
        tiecheck()

def tiecheck():
    count = 0
    for i in board:
        for ii in i:
            if str(ii).isalpha():
                count += 1
    if count == size ** 2:
        print('Winner: None')
        exit()      
board()
printboard()
winning()
