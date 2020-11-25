"""
   * author - ${Suraj Jadhav}
   * date - ${25-Nov-20}
   * time - ${8:00 AM}
   * package - ${PACKAGE_NAME}
   * Title - Write a Program to play a Cross Game or Tic-Tac-Toe Game. Player 1 is the Computer and the Player 2 is the user.
             Player 1 take Random Cell that is the Column and Row..

"""

import random

class tictactoe :
    # construtor
    def __init__(self):
        self.board = {'7':' ','8':' ','9':' ',
                      '4':' ','5':' ','6':' ',
                      '1':' ','2':' ','3':' '}
        self.playerTurn = ''

    def printBoard(self):
        print(self.board['7']+ '|' +self.board['8'] + '|' +self.board['9'])
        print('-+-+-')
        print(self.board['4'] + '|' +self.board['5'] + '|' +self.board['6'])
        print('-+-+-')
        print(self.board['1'] + '|' +self.board['2'] + '|' +self.board['3'])


    def toss(self):
        self.playerTurn = random.randint(0,1)
        if self.playerTurn:
            self.playerTurn = 'X'
            print('Computer Win toss\nYou have O\nComputer have X')
        else:
            self.playerTurn = 'O'
            print('you win toss\nYou have O\nComputer have X')
        return self.playerTurn

    def gameStart(self):
        self.playerTurn = self.toss()
        self.playerTurnCount = 0

        while self.playerTurnCount < 9:
            self.printBoard()

            if self.playerTurn == 'X' :
                print('its computer ' + self.playerTurn + ' Turn\nMove to which place?')
                computerMove = random.randint(1,9)
                move = str(computerMove)
            else:
                print('its your ' + self.playerTurn + ' Turn\nMove to which place?')
                move = input()

            if self.board[move] == ' ':
                self.board[move] = self.playerTurn
                self.playerTurnCount += 1
            else:
                print("That place is already filled.\nMove to which place?")
                continue

            if self.playerTurnCount >= 5:
                if self.board['7'] == self.board['8'] == self.board['9'] != ' ':  # across the top
                    self.printBoard()
                    print("\nGame Over.\n")
                    print("**** " + self.playerTurn + " won. ****")
                    break
                elif self.board['4'] == self.board['5'] == self.board['6'] != ' ':  # across the middle
                    self.printBoard()
                    print("\nGame Over.\n")
                    print("**** " + self.playerTurn + " won. ****")
                    break
                elif self.board['1'] == self.board['2'] == self.board['3'] != ' ':  # across the bottom
                    self.printBoard()
                    print("\nGame Over.\n")
                    print("**** " + self.playerTurn + " won. ****")
                    break
                elif self.board['1'] == self.board['4'] == self.board['7'] != ' ':  # down the left side
                    self.printBoard()
                    print("\nGame Over.\n")
                    print("**** " + self.playerTurn + " won. ****")
                    break
                elif self.board['2'] == self.board['5'] == self.board['8'] != ' ':  # down the middle
                    self.printBoard()
                    print("\nGame Over.\n")
                    print("**** " + self.playerTurn + " won. ****")
                    break
                elif self.board['3'] == self.board['6'] == self.board['9'] != ' ':  # down the right side
                    self.printBoard()
                    print("\nGame Over.\n")
                    print("**** " + self.playerTurn + " won. ****")
                    break
                elif self.board['7'] == self.board['5'] == self.board['3'] != ' ':  # diagonal
                    self.printBoard()
                    print("\nGame Over.\n")
                    print("**** " + self.playerTurn + " won. ****")
                    break
                elif self.board['1'] == self.board['5'] == self.board['9'] != ' ':  # diagonal
                    self.printBoard()
                    print("\nGame Over.\n")
                    print("**** " + self.playerTurn + " won. ****")
                    break
            if self.playerTurnCount == 9:
                print("\nGame Over.\n")
                print("It's a Tie!!")
                self.printBoard()

            if self.playerTurn == 'X':
                self.playerTurn = 'O'
            else:
                self.playerTurn = 'X'


if __name__ == '__main__' :
    try :
        tictactoeObject = tictactoe()
        tictactoeObject.gameStart()
    except :
        print('Exception Raised.')