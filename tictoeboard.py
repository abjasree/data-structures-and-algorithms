theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def printBoard(board):
 print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
 print('-+-+-')
 print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
 print('-+-+-')
 print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'
count = 0
for i in range(10):
    printBoard(theBoard)
    print('Turn for '+turn+'. Move on which space?')
    move = input()
    if theBoard[move] == ' ':
     theBoard[move]=turn
     count += 1
    else:
       print('This position is already taken!!')
       continue
    if count >= 5:
            if theBoard['top-L'] == theBoard['top-M'] == theBoard['top-R']!= ' ': # across the top
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif theBoard['mid-L'] == theBoard['mid-M'] == theBoard['mid-R'] != ' ': # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['low-L'] == theBoard['low-M'] == theBoard['low-R'] != ' ': # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['low-L'] == theBoard['mid-L'] == theBoard['top-L'] != ' ': # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['low-M'] == theBoard['mid-M'] == theBoard['top-M'] != ' ': # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['low-R'] == theBoard['mid-R'] == theBoard['top-R'] != ' ': # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif theBoard['top-L'] == theBoard['mid-M'] == theBoard['low-R'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['low-L'] == theBoard['mid-M'] == theBoard['top-R'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
    if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
 
printBoard(theBoard)
