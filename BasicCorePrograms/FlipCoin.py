"""
   * author - ${Suraj Jadhav}
   * date - ${23-Nov-20}
   * time - ${12:13 AM}
   * package - ${PACKAGE_NAME}
   * Title - Flip Coin and print percentage of Heads and Tails.
"""
import random
class FlipCoin :
    def __init__(self):
        self.FlipCoinNumber = 0
        self.HeadTail = 0
        self.Head = 0
        self.Tail =0

    def NumberOfTimeFlipCoin (self):
        self.FlipCoinNumber = random.randint(5,10)
        print(self.FlipCoinNumber,' Time coin flipped : ')
        for x in range(self.FlipCoinNumber):
            self.HeadTail = random.randint(0,1)
            if self.HeadTail == 0 :
                print('Round ' + str(x+1) + ' H Win')
                self.Head = self.Head + 1
            else :
                print('Round ' + str(x+1) + ' T Win')
                self.Tail = self.Tail + 1
        return self.FlipCoinNumber, self.Head, self.Tail ;

    def CalculatePercentage (self):
        self.FlipCoinNumber, self.Head, self.Tail = self.NumberOfTimeFlipCoin()
        self.Head = self.Head / self.FlipCoinNumber * 100
        self.Tail = self.Tail / self.FlipCoinNumber * 100
        print('Head percentage = ' + str(self.Head))
        print('Tail percentage = ' + str(self.Tail))

    randomNumber = random.randint(1,9)

if __name__ =='__main__' :
    try :
        object = FlipCoin()
        object.CalculatePercentage()
    except :
        print('Exception Occure')