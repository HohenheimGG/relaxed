# Given a positive integer,
# check whether it has alternating bits: namely, if two adjacent bits will always have different values.
#
# Example 1:
# Input: 5
# Output: True
# Explanation:
# The binary representation of 5 is: 101

# Example 2:
# Input: 7
# Output: False
# Explanation:
# The binary representation of 7 is: 111.

# Example 3:
# Input: 11
# Output: False
# Explanation:
# The binary representation of 11 is: 1011.

# Example 4:
# Input: 10
# Output: True
# Explanation:
# The binary representation of 10 is: 1010.

import math

class BinaryNumberWithAlternatingBits(object):
    def solution1(self, num):
        a1 = 1
        temp = self.calculate(a1, num)
        result = math.log(temp, 4)
        if result.is_integer():
            return True
        a1 = 2
        temp = self.calculate(a1, num)
        result = math.log(temp, 4)
        if result.is_integer():
            return True
        return False

    def calculate(self, a1, num):
        return 1 - num * (1 - 4) / a1

if __name__ == '__main__':
    num = 6
    print BinaryNumberWithAlternatingBits().solution1(num)
