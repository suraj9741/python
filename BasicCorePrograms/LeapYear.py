"""
   * author - ${Suraj Jadhav}
   * date - ${23-Nov-20}
   * time - ${1:13 AM}
   * package - ${PACKAGE_NAME}
   * Title - Leap Year.
"""
class LeapYear :
    def __init__(self, Year) :                          # constructor
        self.Year = Year
    def CheckDigit(self):                               # Check user writen Value is 4 digit oe not
        if len(str(self.Year)) == 4:
            if (self.CheckLeapYear()):                  # Calling CheckLeapYear Method
                return f'{self.Year} is Leap Year'
            else :
                return f'{self.Year} is not Leap Year'
        else :
            return f'{self.Year} is not 4 digit number'
    def CheckLeapYear(self):                            # Check Leap Year Method
        if (self.Year % 4) == 0:                        # Check Year divisible by 4 or not
            if (self.Year % 100) == 0:                  # Check Year divisible by 100 or not
                if (self.Year % 400) == 0:              # Check Year divisible by 400 or not
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False



if __name__ == '__main__' :                             # Main Method
    try :                                               # Exception Handling
        year = int(input())                             # Accepting Year from user
        object = LeapYear(year)                         # creating object and pass Parameter
        print(object.CheckDigit())
    except :
        print('Exception Raised.')