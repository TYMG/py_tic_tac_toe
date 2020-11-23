"""
 Tic Tac Toe
"""
symbols = ('X', 'O')
yes_responses = ('Y', 'Yes', 'Si')
no_responses = ('N', 'No')
shut_down_responses = {'quit': 'quit', 'exit': 'exit', 'restart': 'restart'}
player_1 = 'Player 1'
player_2 = 'Player 2'

empty_row = [' ', ' ', ' ']


def tic_tac_toe():
    global symbols
    global yes_responses
    global no_responses
    global shut_down_responses
    global player_1
    global player_2

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
        while row.isdigit() == False:
            row = input('Please enter a Row (1,2,3): ')
            if(row.isdigit() == False):
                print('Please enter a numeric value (1,2,3)')
        row = int(row)
        while col.isdigit() == False:
            col = input('Please enter a Col (1,2,3): ')
            if(col.isdigit() == False):
                print('Please enter a numeric value (1,2,3)')
        col = int(row)
        update_board(game_board, symbol, row-1, col-1)
        print_board(game_board)
        player_1_turn = not player_1_turn
        game_on = False
    return shut_down_responses['exit']


def update_board(game_board, symbol, row, col):
    game_board[row][col] = symbol


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


if __name__ == '__main__':
    tic_tac_toe()
