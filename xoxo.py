import numpy as np

def _new_board():
    ''' Generates a fresh unplayed board '''
    return np.full((3,3),'_')


class GameOver(Exception):
    pass

class Game:
    # game of noughts and crosses
    def __init__(self):
        self.board = _new_board()

    def go(self,piece,place):
        ''' 
        Adds a move to the game board
        raises exception if the move is invalid
        '''
        if self.board[place] != '_':
            print("Bad Move")
            raise ValueError("No move available")
        self.board[place] = piece

        self.check() # check for win


    def get(self):
        return self.board


    def show(self):
        '''
        Print the board state
        '''
        for x in range(3):
            print(self.board[x,:]) # row?
    
    def check(self):
        ''' 
        evaluate the board for a win condition
        '''

        b = self.board
        # rows
        for i in range(3):
            self.test(b[i,:]) # row
            self.test(b[:,i]) # column
        #diagnonals
        self.test([b[0,0],b[1,1],b[2,2]])
        self.test([b[2,0],b[1,1],b[0,2]])
        if '_' not in self.board:
            raise GameOver("Draw")

    def test(self,array):
        if '_' in array:
            return False
        if array[0] == array[1] == array[2]:
            raise GameOver(f"Win for {array[0]}")

class Player:
    ''' xoxo player '''
    def __init__(self,piece,game):
        self.piece = piece
        self.game = game

    def move(self):
        ''' 
        player makes a move
        '''

        #get the board state
        board = self.game.get()
        available_moves =  self.get_available_moves(board)
        place_idx = np.random.randint(0,len(available_moves))
        place = tuple(available_moves[place_idx])
        #decide on a move

        self.game.go(self.piece,place)

    def get_available_moves(self,board):
        ''' return unfilled places'''
        av = np.argwhere(board == '_')
        if len(av) == 0:
            raise GameOver("no available moves")
        return av 
        
          
