# Notakto
def check(board):
    # for 3x3 rows
    for a in range(3):
        cond = True
        # checking column
        for s in range(3):
            if board[a][s] != 'X':
                cond = False
                continue
        if cond == True:
            return cond
    # for 3x3 columns
    for a in range(3):
        cond = True
        # checking row
        for s in range(3):
            if board[s][a] != 'X':
                cond = False
                continue
        if cond == True:
            return cond
    # checking diagonal
    cond = True
    count = 0
    # checking row and column
    for a in range(3):
        if board[a][a] != 'X':
            cond = False
    if cond:
        return cond
    cond = True
    if cond:
        for a in range(3):
            count = 2 - a
            if board[a][count] != 'X':
                cond = False
    return cond

A = [[0,1,2],[3,4,5],[6,7,8]]             
B = [[0,1,2],[3,4,5],[6,7,8]]
C = [[0,1,2],[3,4,5],[6,7,8]]

def winning():                                                  
    if check(A) == True:
        if check(B) == True:
            if check(C) == True:
                return True
    return False

def printboard():                                                         
    if check(A) == False and check(B) == False and check(C) == False: 
                print("A      B      C")                                                 
                for i in range(3):
                    print(*A[i],end="  ")    
                    lst = 7 * 3 + 15                                    
                    print(*B[i],end="  ")
                    lst = 7 * 3 + 15
                    print(*C[i])          
    elif check(A) == False and check(B) == False:                    
            print("A      B")
            for i in range(3):
                print(*A[i],end="  ")
                print(*B[i])  
    elif check(A) == False and check(C) == False:                    
            print("A      C")
            for i in range(3):
                print(*A[i],end="  ")
                print(*C[i])         
    elif check(B) == False and check(C) == False:                   
            print("B      C")
            for i in range(3):
                print(*B[i],end="  ")
                print(*C[i])
    elif check(A) == False:                                        
        print("A")
        for i in range(3):
            print(*A[i])       
    elif check(B) == False:                                       
        print("B")
        for i in range(3):
            print(*B[i])          
    elif check(C) == False:                                       
        print("C")
        for i in range(3):
            print(*C[i])

i = 0                                       

while not winning():                                         
    printboard()
    string = ""
    while True:                                                   
        if i%2==0:                                            
            string = input("Player 1: ")
        else:
            string = input("Player 2: ")
        if string[0]>= "A" and string[0]<="C" and string[1]>="0" and string[1]<="8" and len(string) == 2:  
            board = ""                                           
            x = -1
            y = -1                                          
            if string[0]=="A":                                        
                board = A
            elif string[0] == "B":
                board = B
            else:
                board = C
            x = int(string[1])// (3)                                
            y = int(string[1]) % (3)                                  
            if not check(board) and board[x][y] != "X":  
                board[x][y] = "X"
                break
            else:                                               
                print("Invalid move, please input again")
        else:                                               
            print("Invalid move, please input again")
    i+=1

#Winner of the game
if i%2==0:                                                  
    print("Player 1 wins game")                             
else:
    print("Player 2 wins game")
