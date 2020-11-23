"""
   * author - ${Suraj Jadhav}
   * date - ${23-Nov-20}
   * time - ${10:50 PM}
   * package - ${PACKAGE_NAME}
   * Title - Computes the prime factorization of N using brute force..
"""
import math

class Factors :
    def __init__(self, UserNumber) :                                    # constructor
        self.UserNumber = UserNumber
        self.Factor = 1
    def CalculateFactor(self) :                                         # method for calculating prime factor
        while self.UserNumber % 2 == 0:                                 # print the two and divide by two if remainder is zero
            print ('2'),
            self.UserNumber = self.UserNumber / 2
        for i in range(3, int(math.sqrt(self.UserNumber)) + 1, 2):      # find square root and increment by 2 in range of 3 to squareroot value
            while self.UserNumber % i == 0:
                print(i)
                self.UserNumber = self.UserNumber / i
        if self.UserNumber >2 :                                         # some time prime factor remaining at last so tat will print
            print(int(self.UserNumber))

if __name__ == '__main__' :                                             # main
    try :                                                               # Exception Handling
        UserNumber = int(input('Enter a number : '))                    # accepting Number from User
        object = Factors(UserNumber)                                    # creating object and pass Parameter
        object.CalculateFactor()                                        # Calling Method CalculateFactor
    except :
        print('Exception Raised.')