from player_class import HumanPlayer, RandomComputerPlayer, GeniusAIPlayer
import time

class TicTacToe:
    def __init__(self):
        #define class variables which are accesible by whole class
        #we need a board
        self.board = [' ' for _ in range(9)] # represent board through single list
        self.current_winner = None #keep track of winner

    def print_board(self):
        #need to print each row - so index to get each row
        # i.e. first row is i=0, second row is i=1, third row i=2
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    @staticmethod
    # A static method is bound to a class rather than the objects for that class. 
    # This means that a static method can be called without an object for that class.

    # it doesnt relate to any specific board - we dont need to pass the self arg.
    # i can call TicTacToe.print_board_name() - ie. dont have to instantate!
    def print_board_nums():
        # this defines the layout of the board - which numbers correspond to what box
        # i.e |0|1|2| for the first row
        #.... |3|4|5|
        #.... |6|7|8|
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    
    def avalible_moves(self):
        # add the index of avalible spaces to moves lst
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ') # count number of spaces in board

    def make_move(self, square, letter):
        #to make move we need the square in which to make our move and the letter of
        #the player whos move it is!

        #if valid move, then make the move (assign square to letter)
        # then return true. if unvalid return false!
        
        if self.board[square] == ' ':
            self.board[square] = letter
            #now check for winner
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # winner exist if three in a row! - lets check all!

        row_ind = square // 3 # number of times the square index goes into 3 - i.e 5 // 3 = 1 (2nd row counting from zero)
        row = self.board[row_ind*3 : (row_ind + 1) * 3]

    
        # check row
        if all([spot == letter for spot in row]):
            return True 
        
        # check column
        col_ind = square % 3 ## COOL TRICK to get column ind!!! - counting from zero of course
        column = [self.board[col_ind + i*3] for i in range(3)] #basically just iteratively adding three
        if all([spot == letter for spot in column]):
            return True
        
        #check diag's
        # for a 3x3 board counting from zero - elements in diagals are (0, 2, 4, 6, 8)
        if square % 2 == 0: #i.e. its a diag elm
            diag_1 = [self.board[i] for i in [0, 4, 8]] # left to right diag
            if all([spot == letter for spot in diag_1]):
                return True
            diag_2 = [self.board[i] for i in [2, 4, 6]] # right to left diag
            if all([spot == letter for spot in diag_2]):
                return True
        
        #if all check fail - we dont have a winner 
        return False

def play(game, x_player, o_player, print_game=True):
# returns the winner of the game or None for a tie
    if print_game:
        game.print_board_nums()

    letter ='X' #always start with X

    #iterate while the game still has empty squares
    while game.empty_squares():
        if letter =='O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + ' makes move to square {}'.format(square))
                #lets see what board looks like now!
                game.print_board()
                print('') # print empty space

        if game.current_winner:
            if print_game:
                print(letter + ' WINS!!!')
            return letter

        # need to alternate player
        letter = 'O' if letter =='X' else 'X'

        #have a slight pause to make game play more realistic - rather than instant printout!
        if print_game:
            time.sleep(0.8)

    if print_game:
        print("It's a tie!")


#### just uncoment game you wish to play

## HUMAN vs GENIUS ##
"""if __name__ == '__main__':
    #instantate players
    x_player = HumanPlayer('X')
    o_player = GeniusAIPlayer('O')
    #instantate class
    ttt = TicTacToe()
    #lets play
    play(ttt, x_player, o_player, print_game=True)"""


#let the Genius Play againest each other
if __name__ == '__main__':
    x_genius_wins = 0
    o_genius_wins = 0
    ties = 0
    # run 1000 games

    for _ in range(1000):

        if _ % 100 == 0:
            print(f'{x_genius_wins} X_wins | {o_genius_wins} O_Wins | {ties} Ties')

        #instantate players
        x_player = GeniusAIPlayer('X')
        o_player = GeniusAIPlayer('O')
        #instantate class
        ttt = TicTacToe()
        #lets play
        result = play(ttt, x_player, o_player, print_game=False)

        if result == 'X':
            x_genius_wins += 1
        elif result == 'O':
            o_genius_wins += 1
        else:
            ties += 1
