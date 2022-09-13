import math
import random

#Base class - from which our different players will inherit from
class Player:
    def __init__(self, letter):
        'letter | either X or O representing the player'
        self.letter = letter

    #each player will need to get there next move given a game
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # for the random player we just want to choose a random avalible move!

        #game.availble_moves() returns a lst of avalible moves (index of blank spaces)
        square = random.choice(game.avalible_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        # human player will give their move through an input to the terminal

        # we need to make ure that the input is a valid square
        valid_square = False
        val = None

        while not valid_square:
            #users input
            square = int(input(self.letter + '\'s turn. Input move (0-8):'))
            
            #we need to check whether this valid given is valid
            try:
                ## test 1 ##
                #check that input can be cast to interger - i.e. if user inputs letter then error will be thown and test fails
                val = int(square)

                ## test 2 ##
                #check whether the value is in avalible moves, if not raise a valueError
                if val not in game.avalible_moves():
                    raise ValueError
                
                #if both these tests pass then ---> valid move!
                valid_square = True
                return square
            except ValueError:
                print('Move is not Valid! Try again: ')


#create genius 'AI' Player - who never loses
class GeniusAIPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        
        # randomly assigns first move! 
        if len(game.avalible_moves()) == 9:
            square = random.choice(game.avalible_moves())
        else:
            # use MinMax Algorithm to choose moves!
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        ' state is a snapshot of the current state of the game'
        max_player = self.letter #current player
        other_player = 'O' if player == 'X' else 'X'

        #### base cases ####
        # first we need to check previous move is a winner
        if state.current_winner == other_player:
            return {'position': None,
            'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                state.num_empty_squares() + 1) 
            }
        # no winners and no empty squares - that means nobody has one! 
        elif not state.empty_squares():
            return {'postion': None, 'score' : 0}

        ############################
        ### the MINMAX Algorithm ###
        ############################

        #Initalise - save the best position to move and the best score in dict
        if player == max_player:
            #initalise with ve- inf (because we want to maximise the utility score)
            best = {'position': None, 'score': -math.inf}
        else: # other player - which we want to minimise there utility score - initalise with ve+ inf
            best = {'position': None, 'score': math.inf}

        for possible_move in state.avalible_moves():

            #step 1 | make a move and try that spot
            state.make_move(possible_move, player)

            #step 2 | recurse using minmax to simulate game after making that move
            sim_score = self.minimax(state, other_player) # alternate player

            #step 3 | undo the move 
            state.board[possible_move] = ' ' # undo the move
            state.current_winner = None #reset winner

            sim_score['position'] = possible_move # set the position to that possible move after recursion is finised and utility computed! 
            
            # step 4 | update dict
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score # replace best
                else: # other player
                    if sim_score['score'] < best['score']:
                        best = sim_score
        
        #after every possible move has been scored and utility calculated - lets return the best dict - which has the best possible move and its utility
        return best