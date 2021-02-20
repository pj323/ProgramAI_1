
#Loadboard function is fetching the file and reading the values
#The file is then taken in as array spacing is given.
def loadBoard(grid): 
    inputf = open(grid, 'r')
    board = []
    for r in inputf:
        board.append(r.split())
    return board

#The printboard function is reading every line and printing the value as in text
   
def printBoard(grid):
    for r in grid:
        print(' '.join(map(str,r)))
        
def withinBoundsCheck(length, Position):
#Helper function that returns false if the positions are less than 0 or greater than or equal to the max, N
        
        if Position[0] < 0 or Position[0] > length:
            return False
        
        if Position[1] < 0 or Position[1] > length:
            return False
        return True


#Possible as name suggests it is taking the current position and board
#after fetching the value it is checking in all dirctions from a fixed position
#Here row works as x - cordinate and col as y - cordinates
def possibleMoves(cur_pos,board):
    row = cur_pos[0]
    col = cur_pos[1]
    pos_Array = list()
    if withinBoundsCheck(len(board),cur_pos):
        
        if ( -1 < row < len(board) ) and ( -1 < (col + 1) < len(board)):
            pos_Array.append((row,col+1))
        if ( -1 < (row + 1) < len(board)) and ( -1 < (col + 1) < len(board)):
            pos_Array.append((row+1,col+1))
        if ( -1 < (row + 1) < len(board)) and ( -1 < (col) < len(board)):
            pos_Array.append((row+1,col))
        if ( -1 < (row + 1) < len(board)) and ( -1 < (col - 1) < len(board)):
            pos_Array.append((row+1,col-1))
        if ( -1 < ( row )   < len(board)) and ( -1 < (col - 1) < len(board)):
            pos_Array.append((row,col-1))
        if ( -1 < (row - 1) < len(board)) and ( -1 < (col - 1) < len(board)):
            pos_Array.append((row-1,col-1))
        if ( -1 < (row - 1) < len(board)) and ( -1 < (col) < len(board)):
            pos_Array.append((row-1,col))
        if ( -1 < (row - 1) < len(board)) and ( -1 < (col + 1) < len(board)):
            pos_Array.append((row-1,col+1))
    return(pos_Array)
#the cursor does not take value if condt is false and if it points outside the grid/board
#making sure that the code does not go back to the postion which is already been visited   

#legalmove prints all the positions which are not visited again
def legalMoves(possibleMoves, visited):
    visit = list(visited)
    valid = []
    for i in possibleMoves:
        if i not in visit:
            valid.append(i)

    print(valid)
    
#The examinestate takes the letter gorups it as a word
#the grouped word is then checked in the dictionary checks it in the dictionary 
def examineState(board, cur_pos, cur_path, myDict):
    words = list()
    for i in cur_path:
        row,col = i
        words.append(board[row][col])

    row,col = cur_pos
    words.append(board[row][col])
    
    word = ''.join(map(str,words)) 
    
    print(word.lower())
    
    if word.lower() in myDict:
        print((word.lower() , 'Yes'))
        
    else:
        print((word.lower(), 'No'))
        
        
        
        

# myDict = open("myfile.txt", 'r').read().split("\n")

            
# cur_pos=[0,0]
# diag = ((0,0),(1,1),(2,2),(3,3))
# board=loadboard('matrix.txt')        
# printBoard(board)
# print("Possiblemoves", cur_pos , "board")
# print(Possiblemoves(cur_pos,(board)))
# # print(len(board))
# legalMoves(Possiblemoves(cur_pos, board), diag) 
# cur_path = ((1,1),(1,0))
# examineState(board,cur_pos,cur_path,myDict)