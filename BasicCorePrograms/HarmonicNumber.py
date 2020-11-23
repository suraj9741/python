"""
   * author - ${Suraj Jadhav}
   * date - ${23-Nov-20}
   * time - ${10:50 AM}
   * package - ${PACKAGE_NAME}
   * Title - Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N.
"""
class HarmonicNumber :
    def __init__(self, UserNumber):                                                             # constructor
        self.UserNumber = UserNumber
        self.div = 0
        self.sum = 0
    def HarmonicValue(self):                                                                    # Harmonic Value Calculater
        for i in range(1,(self.UserNumber+1)) :
            self.div = 1/i
            self.sum = self.sum + self.div
        print(self.sum)

if __name__ == '__main__' :                                                                     # Main Method
    try :                                                                                       # Exception Handling
        UserNumber = int(input('Enter the number upto you want to print harmonic value :'))     # accepting Number from User
        object = HarmonicNumber(UserNumber)                                                     # creating object and pass Parameter
        object.HarmonicValue()                                                                  # Calling Method HarmonicValue
    except :
        print('Exception Raised.')