import numpy as  np


# print(len(board))
# print(len(board[0]))
# print(board)

#vals = [8,3,3,3,7,6,0,1,0]

# creating an empty list 
vals = [] 
  
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
  
# iterating till the range 
for i in range(0, n): 
    ele = int(input()) 
  
    vals.append(ele) # adding the element

n=3

# def isSafe(col):
#     if(col>=0 and col < n):
#         return True
#     return False

def solver():
    
    board = [[0 for i in range(n)]for i in range(n)]

    if(not solverUtil(2, vals, board, 0)):
        print("no solution")
    else:
        print(board)

def solverUtil(col, vals, board, carry):
    if(col==-1 and carry!=1):
        return True

    for i in range(len(vals)):
        board[0][col]=vals[i]
        vals.remove(board[0][col])
        for j in range(len(vals)):
            board[1][col]=vals[j]
            vals.remove(board[1][col])
            for k in range(len(vals)):
                board[2][col]=vals[k]
                #print(vals,k)
                print(board)

                vals.remove(board[2][col])
                sol = board[0][col]+board[1][col]+carry
                tempCarry=carry
                if(sol>=10):
                    carry=1
                else:
                    carry=0
                if(sol-10*carry==board[2][col]):
                    if(solverUtil(col-1,vals,board,carry)):
                        return True
                carry=tempCarry

                vals.insert(k,board[2][col])
                #board[2][col]=0
            vals.insert(j,board[1][col])
            #board[1][col]=0
        vals.insert(i,board[0][col])    
        #board[0][col]=0
                    
                     

    return False

solver()






