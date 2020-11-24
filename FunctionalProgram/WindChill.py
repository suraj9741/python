"""
   * author - ${Suraj Jadhav}
   * date - ${24-Nov-20}
   * time - ${10:00 AM}
   * package - ${PACKAGE_NAME}
   * Title - Write a program WindChill that takes two double command-line arguments t and v and prints the wind chill.
             Given the temperature t (in Fahrenheit) and the wind speed v (in miles per hour), the National Weather
             Service defines the effective temperature (the wind chill)
"""
class WindChill :
    def __init__(self) :                                                            # constructor
        self.Temperature = 0
        self.Velocity = 0
        self.windChill = 0
    def AcceptingValue(self) :                                                      # Accept Value in range
        flag = True
        while (flag) :                                                              # Accept Temperature
            self.Temperature = float(input('Enter Temperature in Fahrenheit ragne (less than 50) : '))
            if self.Temperature < 50 :
                flag = False
                print(f'Enter Temperature in rage = {self.Temperature}')
            else :
                print(f'Enter Temperature = {self.Temperature}\nnot in range  \nEnter again ragne (less than 50).')
        flag = True
        while (flag):                                                               # Accept Velocity
            self.Velocity = float(input('Enter Velocity in miles per hour ragne (greter than 3 and less than 120) : '))
            if 3 < self.Velocity < 120:
                flag = False
                print(f'Enter Velocity in rage = {self.Velocity}')
            else:
                print(f'Enter Velocity = {self.Velocity}\nnot in range  \nEnter again ragne (greter than 3 and less than 120).')
    def CalculatewindChill(self) :                                                  # Calculate Wind chill
        self.windChill = 35.74 + (0.6215 * self.Temperature) + (((0.4275 * self.Temperature) - 35.75) * pow(self.Velocity, 0.16))
        print('effective temperature : ',self.windChill)


if __name__ == '__main__' :                                                         # main
    try :                                                                           # Exception Handling
        object = WindChill()                                                        # creating object
        object.AcceptingValue()                                                     # Calling Method AcceptingValue
        object.CalculatewindChill()                                                 # Calling Method CalculatewindChill
    except :
        print('Exception Raised.')