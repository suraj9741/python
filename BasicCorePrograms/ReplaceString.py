"""
   * author - ${Suraj Jadhav}
   * date - ${22-Nov-20}
   * time - ${10:55 PM}
   * package - ${PACKAGE_NAME}
   * Title - User Input and Replace String Template “Hello <<UserName>>, How are you?”
"""
class ReplaceString :
    def __init__(self):                                 # constructor
        self.UserName = " "
    def main(self):                                     # Method To Accepting and check the min character condition
        self.UserName = input("Enetr the User Name : ")
        Lenght = len(self.UserName)
        if Lenght > 3 :
            print ('Hello '+ self.UserName +', How are you?')
        else :
            print('Enter min 3 char')

if __name__ == '__main__':                              # Main method
    try :                                               # Exception Handling
        object = ReplaceString()
        object.main()
    except :
        print('Exception Raised.')
