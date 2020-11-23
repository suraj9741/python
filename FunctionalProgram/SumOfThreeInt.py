"""
   * author - ${Suraj Jadhav}
   * date - ${24-Nov-20}
   * time - ${12:50 AM}
   * package - ${PACKAGE_NAME}
   * Title - A program with cubic running time. Read in N integers and counts the number of triples that sum to exactly 0.
"""

class SumOfThreeInt :
    def __init__(self) :                                                        # constructor
        self.ListLenght = 0
        self.List = []
        self.Flag = False
    def AcceptingListValue(self) :                                              # Accepting List Number
        self.ListLenght = int(input('How many element you wnat to enter :'))
        print('Enter the number :')
        for i in range(self.ListLenght) :
            self.List.append(int(input()))
        print (self.List)
    def FindTriplets(self):                                                     # Find Triplate Method
        for i in range(0, self.ListLenght - 2):
            for j in range(i + 1, self.ListLenght - 1):
                for k in range(j + 1, self.ListLenght):
                    if (self.List[i] + self.List[j] + self.List[k] == 0):
                        print(self.List[i], self.List[j], self.List[k])         # Print Triplets
                        found = True
        if (found == False):                                                    # If no triplet with 0 sum found in array
            print(" not exist ")

if __name__ == '__main__' :                                                     # main
    try :                                                                       # Exception Handling
        object = SumOfThreeInt()                                                # creating object
        object.AcceptingListValue()                                             # Calling Method AcceptingListValue
        object.FindTriplets()                                                   # Calling Method FindTriplets
    except :
        print('Exception Raised.')