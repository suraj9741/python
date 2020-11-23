"""
   * author - ${Suraj Jadhav}
   * date - ${23-Nov-20}
   * time - ${10:13 AM}
   * package - ${PACKAGE_NAME}
   * Title - This program takes a command-line argument N and prints a table of the powers of 2 that are less than or equal to 2^N.
"""
class PowerOf2 :
    def __init__(self, UserNumber):                 # constructor
        self.UserNumber = UserNumber
        self.Power = 1
    def CheckUserNumber(self):                      # Check the range in between 0 <= Number < 31
        if 0 <= self.UserNumber < 31 :
            self.PowerTable()                       # Calling Method PowerTable
        else :
            print('Overflows int / Out of range')
    def PowerTable(self) :                          # Print Power of 2 table
        for i in range(self.UserNumber+1) :
            self.Power = pow(2,i)                   # pow(2,3) = (2*2*2) its power function
            print(f'2^{i} =',self.Power)

if __name__ == '__main__' :                         # Main Method
    try :                                           # Exception Handling
        UserNumber = int(input())                   # accepting Number from User
        object = PowerOf2(UserNumber)               # creating object and pass Parameter
        object.CheckUserNumber()                    # Calling Method CheckUserNumber
    except :
        print('Exception Raised.')