"""
 Tic Tac Toe
"""
symbols = ('X', 'O')
yes_responses = ('Y', 'Yes', 'Si')
no_responses = ('N', 'No')
shut_down_responses = {'quit': 'quit', 'exit': 'exit', 'restart': 'restart'}
player_1 = 'Player 1'
player_2 = 'Player 2'
turns = 0

diagonal_checks = ((0, 0), (0, 2), (1, 1), (2, 0), (2, 2))

empty_row = [' ', ' ', ' ']


def tic_tac_toe():
    global symbols
    global yes_responses
    global no_responses
    global shut_down_responses
    global player_1
    global player_2
    global turns

    running = True
    users = {player_1: '', player_2: ''}
    while running:
        resp = input(
            "Welcome to Tic Tac Toe!!! \nDo you want to play a game? [Y/N]: \n")
        if resp in yes_responses:
            while True:
                resp = input("Ok Player 1 select a symbol: X or O ")
                resp = resp.upper()
                if resp in symbols:
                    set_player_symbol(users, resp)
                    print(
                        f'Ok Player 1 is {users[player_1]} and Player 2 is {users[player_2]}')
                    break
                else:
                    print('Sorry that is not a valid input.\nPlease enter X or O\n')
            turns = 1
            result = game(users)
            if result == shut_down_responses['exit']:
                running = False
            else:
                continue
        elif resp in no_responses:
            print('Ok, maybe next time!\nSee ya later')
            break
        else:
            print('Sorry that is not a valid input.\nPlease enter Y or N\n')


def set_player_symbol(users, symbol):
    global symbols
    global player_1
    global player_2

    if symbol == symbols[0]:
        users[player_1] = symbols[0]
        users[player_2] = symbols[1]
    else:
        users[player_1] = symbols[1]
        users[player_2] = symbols[0]
    return users


def game(users):
    global shut_down_responses
    global player_1
    global player_2

    game_on = True
    player_1_turn = True
    game_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    print('\nStarting Game' + '...'*4)
    print_board(game_board)
    while game_on:
        is_up = ' is up'
        symbol = None
        if player_1_turn:
            print(f"{player_1}"+is_up)
            symbol = users[player_1]
        elif player_1_turn == False:
            print(f"{player_2}"+is_up)
            symbol = users[player_2]
        row = ''
        col = ''
        while True:
            while row.isdigit() == False:
                row = input('Please enter a Row (1,2,3): ')
                if(row.isdigit() == False):
                    print('Please enter a numeric value (1,2,3)')
            row = int(row)
            while col.isdigit() == False:
                col = input('Please enter a Col (1,2,3): ')
                if(col.isdigit() == False):
                    print('Please enter a numeric value (1,2,3)')
            col = int(col)
            print(f'{col},{row}')
            if game_board[row-1][col-1] == ' ':
                break
            print('Cell has already be taken, please enter another Row and Col\n')
            row = ''
            col = ''
        game_on = update_board(game_board, symbol, (row-1, col-1),
                               player_1 if player_1_turn else player_2)
        player_1_turn = not player_1_turn
        print_board(game_board)
    return shut_down_responses['exit']


def update_board(game_board, symbol, coor, player):
    global turns

    turns += 1
    game_board[coor[0]][coor[1]] = symbol
    is_winner = check_for_winner(game_board, coor, symbol)
    if is_winner:
        print_winner(player)
        return False
    if turns == 10:
        tie_winner()
        return False
    return True


def check_for_winner(game_board, coor, symbol):
    global diagonal_checks
    symbol_list = [symbol]*3
    '''
    From coor passed:
        Check Verticle (-1,0,1)
        Horizontal (-1,0,1)
        Diagonal (-1,0,1) and (1)
    '''
    winner = False
    if game_board[coor[0]] == symbol_list:
        winner = True
    verticleBoard = [row[coor[1]] for row in game_board]
    if verticleBoard == symbol_list:
        winner = True
    if coor in diagonal_checks:
        if [game_board[0][0], game_board[1][1], game_board[2][2]] == symbol_list or [game_board[0][2], game_board[1][1], game_board[2][0]] == symbol_list:
            winner = True
    return winner


def print_board(game_board):

    seperator = '-------------'
    print('\n'+seperator)
    for values in game_board:
        print('| {0:2}| {1:^2}| {2:2}|'.format(
            values[0], values[1], values[2]))
        print(seperator)
    print('\n')


def print_winner(victor):
    print(f'{victor} is the winner!!!')


def tie_winner():
    print(f'We have a tie !!! ¯\_(ツ)_/¯ ')


def test_logic():
    game_board = [['X', 'X', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]
    if game_board[0] == ['X']*3:
        print('Horizontal')
    game_board = [['X', ' ', ' '], ['X', ' ', ' '], ['X', ' ', ' ']]
    verticleBoard = [row[0] for row in game_board]
    print(verticleBoard)
    if verticleBoard == ['X']*3:
        print('Verticle')
    game_board = [['X', ' ', ' '], [' ', 'X', ' '], [' ', ' ', 'X']]
    if [game_board[0][0], game_board[1][1], game_board[2][2]] == ['X']*3:
        print('Diagonal')
    game_board = [[' ', ' ', 'X'], [' ', 'X', ' '], ['X', ' ', ' ']]
    if [game_board[0][2], game_board[1][1], game_board[2][0]] == ['X']*3:
        print('Diagonal Again')


def checkInDiagonal():
    global diagonal_checks
    if (0, 0) in diagonal_checks:
        print('TRUE')


if __name__ == '__main__':
    tic_tac_toe()
    # test_logic()
    # checkInDiagonal()
