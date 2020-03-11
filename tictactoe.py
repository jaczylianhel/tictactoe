## DEF

def clearOutput():
    from IPython.display import clear_output
    clear_output()

def clearBoard():
    
    print('1' + '|' + '2' + "|" + '3')
    print('4' + '|' + '5' + "|" + '6')
    print('7' + '|' + '8' + "|" + '9')
    
    
def printBoard(board,moviePlayer1,moviePlayer2,player1,player2):
    board[moviePlayer1-1] = player1
    board[moviePlayer2-1] = player2
    clearOutput() #clear board
    print(board[0] + '|' + board[1] + "|" + board[2])
    print(board[3] + '|' + board[4] + "|" + board[5])
    print(board[6] + '|' + board[7] + "|" + board[8])
    print('\n')

    
def startGame(inputYorN):

    askEnter = ""
    
    while askEnter != True:
        if inputYorN == 'Y':
            print('Enter Y')
            askEnter = True
            return True
        elif inputYorN == 'N':
            print('Exit from program ...')
            break
        else:
            print('Wrong letter, please enter again...')          
            inputYorN  = input("Begin? Y/N: ").upper()
            
def selectPlayer(inputXorO):
    player1=""
    player2=""
    while player1 != 'X' and player1 != 'O':
        if inputXorO == 'X':
            print('Enter X')
            player1 = 'X'
            player2 = 'O'
        elif inputXorO == 'O':
            print('enter O')
            player1 = 'O'
            player2 = 'X'
        else:
            print('Wrong letter, please enter again...')
            inputXorO = input("Select X or O: ").upper()
    return (player1, player2)

def dFirstPlayerMovie(movie,tablePlayer1,tablePlayer2):                 
    correct=True
    while correct:
        moviePlayer1 = int(input("Player1: enter the number 1-9 "))
        if (moviePlayer1 > 9) or (moviePlayer1 < 1):
            print('Enter number again')
        elif (moviePlayer1 in tablePlayer1) or (moviePlayer1 in tablePlayer2): #check wrong turn Player1
            print("It's not empty blank")
        else:
            correct=False
    movie +=1
    return (moviePlayer1,movie)

def turnPlayer1(runPlayer1,movie,tablePlayer1,tablePlayer2): 
    while runPlayer1: # MOVIE PLAYER 1
        moviePlayer1,movie=dFirstPlayerMovie(movie,tablePlayer1,tablePlayer2)
        runPlayer1=False
    print(f'\nPlayer 1 enter {moviePlayer2}, movie: {movie}\n') 
    return(moviePlayer1, movie)
    


def dSecondPlayerMovie(movie,tablePlayer1,tablePlayer2):  
    correct=True
    while correct:
        moviePlayer2 = int(input("Player2: enter the number 1-9 "))
        if (moviePlayer2 > 9) or (moviePlayer2 < 1):
            print('Enter number again')
        elif (moviePlayer2 in tablePlayer1) or (moviePlayer2 in tablePlayer2): #check wrong turn Player1
            print("It's not empty blank")
        else:
            correct=False
    movie +=1
    return (moviePlayer2,movie)
        

def turnPlayer2(runPlayer2,movie,tablePlayer1,tablePlayer2):
    while runPlayer2: # MOVIE PLAYER 2
        moviePlayer2,movie=dSecondPlayerMovie(movie,tablePlayer1,tablePlayer2)
        runPlayer2=False
    print(f'\nPlayer 2 enter {moviePlayer2}, movie: {movie}\n')
    return(moviePlayer2, movie)
     
        
def checkWinPlayerOne(winGameTable,tablePlayer1,hit,endGame):
    for x in range(0,len(winGameTable)):
        for y in winGameTable[x]:
            if y in tablePlayer1:
                hit +=1
        if hit == 3:
            endGame = True
        else:
            hit=0
    if endGame:
        print('End game, Player 1 wins')
        
    return endGame
                
def checkWinPlayerTwo(winGameTable,tablePlayer2,hit,endGame):
    for x in range(0,len(winGameTable)):
        for y in winGameTable[x]:
            if y in tablePlayer2:
                hit +=1
        if hit == 3:
            endGame = True
        else:
            hit=0
    if endGame:
        print('End game, Player 2 wins')
    return endGame
                
def checkTieGame(movie,endGame):
    if movie == 9:
        print('Tie Game')
        endGame=True
    return endGame


######################## GAME

inputYorN  = input("Begin? Y/N: ").upper()
enterGame = startGame(inputYorN) 

while enterGame:
    winGame = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    game = True
    endGame = False
    movie = 0
    hit = 0
    runPlayer1 = True 
    runPlayer2 = False
    countWin = 0
    winPlayer1 = 0
    winPlayer2 = 0
    
    inputCountWin = int(input("How many wins?"))
    print(inputCountWin)
    while winPlayer1 <inputCountWin and winPlayer2 <inputCountWin:
    
        inputXorO = input("Select X or O: ").upper()  #ask about X or O
        board = [" "]*10
        tablePlayer1 = []
        tablePlayer2 = []
        moviePlayer1 = ""
        moviePlayer2 = 10
        player1,player2 = selectPlayer(inputXorO) #execute and return x or O

        clearBoard() # print a clear table
        while game:

            moviePlayer1,movie = turnPlayer1(runPlayer1,movie,tablePlayer1,tablePlayer2) ## return movie (1-9) and turn(count)      
            printBoard(board,moviePlayer1,moviePlayer2,player1,player2) #Print movie player1
            tablePlayer1.append(moviePlayer1) ##create table with shot player1

            if checkWinPlayerOne(winGame,tablePlayer1,hit,endGame): #check win Player1 ?
                winPlayer1+=1
                break
            if checkTieGame(movie,endGame):
                break

            runPlayer2 = True

            moviePlayer2,movie=turnPlayer2(runPlayer2,movie,tablePlayer1,tablePlayer2) # return movie (1-9) and turn(count)
            printBoard(board,moviePlayer1,moviePlayer2,player1,player2) #Print movie player2
            tablePlayer2.append(moviePlayer2) ##create table with shot player1

            if checkWinPlayerTwo(winGame,tablePlayer2,hit,endGame): #check win Player1 ?
                winPlayer2+=1
                print(f'Player1 wins: {winPlayer1}')
                break
            runPlayer1=True

    if startGame(input("Again? Y/N: ").upper()):
        clearOutput() #clear board
        continue
    else:
        enterGame = False

