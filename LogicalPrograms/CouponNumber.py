"""
   * author - ${Suraj Jadhav}
   * date - ${25-Nov-20}
   * time - ${10:30 AM}
   * package - ${PACKAGE_NAME}
   * Title - Given N distinct Coupon Numbers, how many random numbers do you need to generate distinct coupon number?
            This program simulates this random process.


"""

import random

class generateCoupen :

    def get_promo_code(self, num_chars):
        code_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        code = ''
        for i in range(0, num_chars):
            slice_start = random.randint(0, len(code_chars) - 1)
            code += code_chars[slice_start]
        return code

    def checkUniqcode(self):
        coupenCount = int(input('Enter number how many coupon you required : '))
        coupenLength = int(input('how much length you required for coupon :'))
        couponList = []
        for i in range(coupenCount):
            coupon = self.get_promo_code(coupenLength)
            # print(coupon)
            couponList.insert(i, coupon)
        print(couponList)

if __name__ == '__main__' :
    objectCoupenCode = generateCoupen()
    objectCoupenCode.checkUniqcode()