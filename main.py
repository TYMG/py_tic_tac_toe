"""
 Tic Tac Toe
"""
symbols = ('X', 'O')
yes_responses = ('Y', 'Yes', 'Si')
no_responses = ('N', 'No')
shut_down_responses = {'quit': 'quit', 'exit': 'exit', 'restart': 'restart'}
player_1 = 'Player 1'
player_2 = 'Player 2'

seperator = '------------'
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
            result = game_on(users)
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


def game_on(users):
    global shut_down_responses

    game_board = ['', '', '']*3
    print('\nStarting Game' + '...'*4)
    print(game_board)
    return shut_down_responses['exit']


if __name__ == '__main__':
    tic_tac_toe()
