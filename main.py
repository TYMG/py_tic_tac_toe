"""
 Tic Tac Toe
"""
yesResponses = ['Y', 'Yes', 'Si']
noResponses = ['N', 'No']
shutDownResponses = ['quit', 'exit']
seperator = '------------'
player1 = 'Player 1'
player2 = 'Player 2'


def ticTacToe():
    global yesResponses
    global noResponses
    global shutDownResponses
    global player1
    global player2

    running = True
    users = {player1: '', player2: ''}
    while running:
        resp = input(
            "Welcome to Tic Tac Toe!!! \nDo you want to play a game? [Y/N]: \n")
        if resp in yesResponses:
            # running = False
            break
        elif resp in noResponses:
            print('Ok, maybe next time!\nSee ya later')
            break
        else:
            print('Sorry that is not a valid input.\nPlease enter Y or N\n')


def printHW():
    print('Hello World')


if __name__ == '__main__':
    ticTacToe()
