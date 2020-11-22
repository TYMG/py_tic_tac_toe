"""
 Tic Tac Toe
"""


def ticTacToe():
    running = True
    yesResponses = ['Y', 'Yes', 'Si']
    while running:
        quit = input("Do you want to quit?:  ")
        print(f'{quit}')
        if quit in yesResponses:
            running = False


def printHW():
    print('Hello World')


if __name__ == '__main__':
    ticTacToe()
