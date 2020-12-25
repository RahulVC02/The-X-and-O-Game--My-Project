import random #Used to generate a random function
from playsound import playsound #installed library for playing sounds
import sys #importing the sys module
board=[i for i in range(0,9)] #creating a board list
player, computer = '',''
winners=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))#These combinations make you win
moves=((5,),(1,7,3,9),(2,4,6,8))#Center,corner and inner diamond positions
name=input('Enter your name to play the game:')
print("If you can beat me at this,I'll play a song")
tab=range(1,10)#Table is a list of numbers from 1 to9


def select_char(): #Function used to select a character(either X or 0) that you will use.
                   #The other will be used by the computer.
    chars=('X','O')
    if random.randint(0,1) == 0:# Here, I have used the random function to randomly assign X or 0 to the player.
        return chars[::-1]
    return chars
def can_win(brd, player, move): #This function returns a Boolean value everytime the board is analyzed
                                #It makes the computer decide if it can win or not.
    places=[]
    x=0
    for i in brd:
        if i == player: places.append(x);
        x+=1
    win=True
    for tup in winners:
        win=True
        for ix in tup:
            if brd[ix] != player:
                win=False
                break
        if win == True:
            break
    return win


def can_move(brd, player, move): #Function used to check the validity of a move if it lies in tab
    if move in tab and brd[move-1] == move-1:
        return True   #Only one of the return statements will be executed as a function
    return False      #returns only one value

def make_move(brd, player, move, undo=False): #This function is used within the computer_move function to
                                              #generate the computer's response.
    if can_move(brd, player, move):
        brd[move-1] = player
        win=can_win(brd, player, move)
        if undo:
            brd[move-1] = move-1
        return (True, win)
    return (False, False)

def space_exist():#This function is used to check if the number of Os and Xs don't sum up to 9
    return board.count('X') + board.count('O') != 9
def print_board(): #Function that will print a board for X an 0
    x=1
    for i in board:
        end = ' | '
        if x%3 == 0:#Every value of x divisible by 3
            end = ' \n'
            if i != 1: end+='---------\n';
        char=' '
        if i in ('X','O'): char=i;
        x+=1
        print(char,end=end)
#The concepts and ideas for the following code for the computer's response has been borrowed from parts of the StackOverflow website.
#Due acknowledgement is given in the Project Report where i have attached the link
def computer_move():
    move=-1
    #If i can win,others don't matter.
    for i in range(1,10):
        if make_move(board, computer, i, True)[1]:
            move=i
            break
    if move == -1:
       # If player can win, block him.
        for i in range(1,10):
            if make_move(board, player, i, True)[1]:
                move=i
                break
    if move == -1:
        # Otherwise, try to take one of desired places.
        for tup in moves:
            for mv in tup:
                if move == -1 and can_move(board, computer, mv):
                    move=mv
                    break
    return make_move(board, computer, move)
#The borrowed code ends over here.
player, computer = select_char()
print('Player is [%s] and computer is [%s]' % (player, computer))
result='CONGRATULATIONS.YOU MANAGED TO DRAW WITH ME,'#Statement that is printed when a tie occurs.
file=('C:\\Users\\Rahul Chembakasseril\\PycharmProjects\\pythonProject\\venv\\Deuce.mp3')#I have used
#the playsound module and chosen this mp3 file to playin case of a draw.
#The function is passed the file path as a parameter.
while space_exist():#Here, the loop will run so long as the space_exist function returns True- the board is not empty
    print_board()
    print('#Make your move ! [1-9] : ', end='')
    #playsound('C:\\Users\\Rahul Chembakasseril\\PycharmProjects\\pythonProject\\venv\\Rolling Dice.mp3')
    #Due to technical issues on syncing audio with GitHub this audio cannot be played right now. I have shown that
#it works during the demo during my presentation when I ran the program on my IDE-PyCharm
    #I have used the playsound module once more and passed the file path everytime the user must take input.
    move = int(input())
    moved, won = make_move(board, player, move)
    if not moved:
        print(' >> Invalid number ! Try again !')#In case the user inputs an invalid or unwanted input.
        continue                                 #that has already been occupied in the grid.

    if won:
        result='ALAS!YOU HAVE DEFEATED ME,' #Here i have used the variable result to print a statement
                                           #in the end.
        file="C:\\Users\\Rahul Chembakasseril\\PycharmProjects\\pythonProject\\venv\\Wiining Effect.mp3"
        #I have used the file variable to pass as a parameter to the playsound function at the end.
        break
    elif computer_move()[1]:
        result='YOU HAVE LOST TO ME!'#Here i have used the variable result to print a statement
                                           #in the end.
        file="C:\\Users\\Rahul Chembakasseril\\PycharmProjects\\pythonProject\\venv\\Losing Effect.wav"
        # I have used the file variable to pass as a parameter to the playsound function at the end.
        break
print_board() #This will help to print the board each time the user gives input
              #and the computer responds.
#playsound(file)#This command will either run the winning track or losing track
#Due to technical issues on syncing audio with GitHub this audio cannot be played right now. I have shown that
#it works during the demo during my presentation when I ran the program on my IDE-PyCharm

print(result,name,".")#This prints the win or loss result.
print('Re-run to play once more.')