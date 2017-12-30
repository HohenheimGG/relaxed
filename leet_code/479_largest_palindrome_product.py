# Find the largest palindrome made from the product of two n-digit numbers.
#
# Since the result could be very large, you should return the largest palindrome mod 1337.
#
# Example:
#
# Input: 2
#
# Output: 987
#
# Explanation: 99 x 91 = 9009, 9009 % 1337 = 987
#
# Note:
#
# The range of n is [1,8].

import math

class LargestPalindromeProduct(object):
    def solution1(self, n):
        if n == 1:
            return 9
        upper = math.pow(10, n) - 1
        lower = upper / 10 + 1
        maxNumber = upper * upper
        half = maxNumber / math.pow(10, n)
        hasPalindrome = False
        palindrome = 0

        while not hasPalindrome:
            palindrome = self.createPalindrome(half)
            for i in range(upper, lower - 1, -1):
                if i * i < palindrome:
                    break
                if palindrome % i == 0:
                    hasPalindrome = True
            half -= 1
        return palindrome % 1337

    def createPalindrome(self, half):
        return half[::-1]