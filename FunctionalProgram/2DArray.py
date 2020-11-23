"""
   * author - ${Suraj Jadhav}
   * date - ${23-Nov-20}
   * time - ${11:50 PM}
   * package - ${PACKAGE_NAME}
   * Title - A library for reading in 2D arrays of integers, doubles, or booleans from standard input and printing them out to standard output.
"""

class TwoDArray :
    def __init__(self, Row, Column) :                               # constructor
        self.Row = Row
        self.Column = Column
        self.TwodArray =[]
        print(self.Row, self.Column)
    def EnterTheValue(self) :                                       # Enter Value in 2D Array
        print("Enter the entries rowwise : ")
        for i in range(self.Row):                                   # A for loop for row entries
            print ((i+1),' Row')
            a = []
            for j in range(self.Column):                            # A for loop for column entries
                value = int(input())
                a.append(value)
            self.TwodArray.append(a)
    def PrintTwodArray(self):                                       # Printing 2D Array
        for i in range(self.Row):
            for j in range(self.Column):
                print(self.TwodArray[i][j], end = " ")
            print()
if __name__ == '__main__' :                                         # main
    try :                                                           # Exception Handling
        Row = int(input('Enter the number of Rows : '))             # accepting Row Number from User
        Column = int(input('Enter the number of Columns : '))       # accepting Column Number from User
        object = TwoDArray(Row, Column)                             # creating object and pass Parameter
        object.EnterTheValue()                                      # Calling Method EnterTheValue
        object.PrintTwodArray()                                     #  Calling Method PrintTwodArray
    except :
        print('Exception Raised.')
