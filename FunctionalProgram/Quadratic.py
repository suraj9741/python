"""
   * author - ${Suraj Jadhav}
   * date - ${24-Nov-20}
   * time - ${9:30 AM}
   * package - ${PACKAGE_NAME}
   * Title - Write a program to find the roots of the equation a*x*x + b*x + c. Since the equation is x*x, hence there
            are 2 roots.
"""
import math

class Quadratic :
    def __init__(self) :                                                                        # constructor
        self.a = 0
        self.b = 0
        self.c = 0
        self.root1 = 0
        self.root2 = 0
        self.delta = 0
    def AcceptingValue(self) :
        self.a = int(input('Enter a in ( aX^2 + bX + c ) : '))                                  # Accepting a from equation
        self.b = int(input('Enter b in ( aX^2 + bX + c ) : '))                                  # Accepting b from equation
        self.c = int(input('Enter c in ( aX^2 + bX + c ) : '))                                  # Accepting c from equation
        print(f'Equation is : {self.a}X^2 + {self.b}X + {self.c}')                              # print equation
    def Calculation(self) :
        self.delta = (self.b * self.b) - (4 * self.a * self.c)                                  # Calculate delta
        self.root1 = (-self.b + math.sqrt(self.delta)) / (2 * self.a)                           # Calculate Root 1
        self.root2 = (-self.b - math.sqrt(self.delta)) / (2 * self.a)                           # Calculate Root 2
        print(f'Delta is {self.delta} \nRoot 1 of x : {self.root1} \nRoot 2 of x : {self.root2}')

if __name__ == '__main__' :                                                                     # main
    try :                                                                                       # Exception Handling
        object = Quadratic()                                                                    # creating object
        object.AcceptingValue()                                                                 # Calling Method AcceptingValue
        object.Calculation()                                                                    # Calling Method Calculation
    except :
        print('Exception Raised.')