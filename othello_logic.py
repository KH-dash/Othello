#  Kent Han 23271274.  ICS 32 Lab sec 8.  Project 4.

NONE = '.'
BLACK = 'B'
WHITE = 'W'




def create_new_state(COLUMNS, ROWS) ->list:
    board = []

    for r in range(ROWS):
        row = []
        for c in range(COLUMNS):
            row.append(NONE)
        board.append(row)
    return board

def first_4(COLUMNS, ROWS, tl) ->list:
    board = create_new_state(COLUMNS, ROWS)
    right = int((len(board) + 1) / 2)
    left = right - 1
    bottom = int((len(board[0]) + 1) /2)
    top = bottom - 1
    if tl == 'W':
        p1 = BLACK
        p2 = WHITE
    elif tl == 'B':
        p1 = WHITE
        p2 = BLACK
    board[right][top] = p1
    board[left][bottom] = p1
    board[left][top] = p2
    board[right][bottom] = p2
    return board

def opposite_player(player: str) ->str:
    if player == 'W':
        return 'B'
    elif player == 'B':
        return 'W'


class State:
    def __init__(self, info):
        self._board = first_4(info['COLUMNS'],
                              info['ROWS'], info['tl'])
        self._bscore = 2
        self._wscore = 2
        self._scores = {'B': self._bscore,
                       'W': self._wscore}
        self._turn = info['m1']

    def game_over(self) ->bool:
        return State.poss_moves(self, BLACK) == [] and State.poss_moves(self, WHITE) == []
    
    def winnerg(self) ->str:
        if State.game_over(self):
            if self._scores['B'] > self._scores['W']:
                return 'BLACK'
            elif self._scores['B'] > self._scores['B']:
                return 'WHITE'
        else:
            return NONE

    def winnerl(self) ->str:
        if State.game_over(self):
            if self._scores['B'] < self._scores['W']:
                return 'BLACK'
            elif self._scores['B'] < self._scores['B']:
                return 'WHITE'
        else:
            return NONE

    def winner(self) ->str:
        if self._win == 'G':
            return State.winnerg(self)
        elif self._win == 'L':
            return State.winnerl(self)
    def turn(self) ->str:
        return self._turn

    def turn_name(self) ->str:
        if self._turn == 'B':
            return 'BLACK'
        elif self._turn == 'W':
            return 'WHITE'

    def board(self) ->list:
        return self._board

    def scores(self) ->dict:
        return self._scores

    def whats_here(self, column, row) ->str:
        player = self._board[row][column]
        return player
    
    def change(self, column, row, player) ->None:
        self._board[row][column] = player
        return None

    def on_board(self, column, row) -> bool:
        return column in range(len(self._board)) and row in range(len(self._board[0]))

    def look(self, column, row, player, vert, horiz) ->list:
        pieces = []
        co = column
        ro = row
        while State.on_board(self, co, ro):
            if self._board[ro][co] != NONE:
                pieces.append({'finding' :self._board[ro][co],
                               'column': co, 'row': ro})
                if self._board[ro][co] == player:
                    break
            else:
                break
            co += horiz
            ro += vert

        return pieces

    def if_move(self, column, row, player) ->list:
        increments = [-1, 0, 1]
        valid_flip = []
        for iho in increments:
            for ive in increments:
                if ive == 0 and iho == 0:
                    pass
                elif State.on_board(self, column + iho, row + ive):
                    if self._board[row + ive][column + iho] == opposite_player(player):
                        di = State.look(self, column + iho, row + ive, player, ive, iho)
                        if di[-1]['finding'] == player:
                            valid_flip.extend(di[:-1])
        return valid_flip
    
    def move(self, column, row, player) ->None:
        moves = State.poss_moves(self, player)
        if moves == []:
            self._turn = opposite_player(player)
            return None
        elif {'column': column, 'row': row} in moves:
            flip = State.if_move(self, column, row, player)
            for p in flip:
                State.change(self, p['column'], p['row'], opposite_player(p['finding']))
                self._scores[player] += 1
                self._scores[opposite_player(player)] -= 1
            State.change(self, column, row, player)
            self._scores[player] += 1
            self._turn = opposite_player(player)
        else:
            raise Exception
        return None

    def poss_moves(self, player) ->list:
        moves = []
        for r in range(len(self._board)):
            for c in range(len(self._board[0])):
                if self._board[r][c] == NONE:
                    if State.if_move(self, c, r, player) != []:
                        moves.append({'column': c, 'row': r})
        return moves
                    

    
                        
    



    



        


