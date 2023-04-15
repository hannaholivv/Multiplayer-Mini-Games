# n-Queen
def boards():
    global num
    num = int(input('n: '))
    global board
    board = []
    if num > 3 and num < 11:
        for i in range(num):
            lst = list(range(num*i,num*i+num)) 
            board.append(lst)
        for ii in board:
            for iii in ii[:-1]:
                print(str(iii).rjust(2), end = ' ')
            print(str(ii[-1]).rjust(2))
            
def changequeen():
    queen = input('Queens: ').split()
    queen = list(map(int, queen))
    for i in board:
        for ii in i:
            for iii in queen:
                if iii == ii:
                    board[iii // num][iii % num] = 'Q'
    for ii in board:
        for iii in ii[:-1]:
            print(str(iii).rjust(2), end = ' ')
        print(str(ii[-1]).rjust(2))
        
def check():
    count = 0
    for i in board: #check row
        for ii in i:
            if ii == 'Q':
                count += 1
        if count > 1:
            print('--> FAIL <--')
            exit()
        count = 0

    for i in range(num):
        for ii in range(num):
            if board[ii][i] == 'Q':
                count += 1
        if count > 1:
            print('--> FAIL <--')
            exit()
        count = 0
    
    for i in range(num): #diagonal
        for ii in range(num): 
            if board[i][ii] == 'Q':
                for iii in range(num):
                    for iiii in range(num):
                        if (i != iii and ii != iiii) and ((i + ii == iii + iiii) or (ii - i == iiii - iii)):
                            if board[iii][iiii] == 'Q':
                                print('--> FAIL <--')
                                exit()

    print('--> SUCCESS <--')



boards()
changequeen()
check()

