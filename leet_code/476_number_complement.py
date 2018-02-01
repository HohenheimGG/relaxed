# coding: utf-8
# Given a positive integer, output its complement number.
# The complement strategy is to flip the bits of its binary representation.
#
# Note:
# The given integer is guaranteed to fit within the range of a 32-bit signed integer.
# You could assume no leading zero bit in the integer’s binary representation.
# Example 1:
# Input: 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits),
# and its complement is 010. So you need to output 2.
# Example 2:
# Input: 1
# Output: 0
# Explanation: The binary representation of 1 is 1 (no leading zero bits),
# and its complement is 0. So you need to output 0.

# 1 01   => 0    0
# 2 10   => 01   1
# 3 11   => 00   0
#
# 4 100  => 011  3
# 5 101  => 010  2
# 6 110  => 001  1
# 7 111  => 000  0
#
# 8  1000 => 0111 7
# 9  1001 => 0110 6
# 10 1010 =>      5
# 11 1011         4
# 12 1100         3
# 13 1101         2
# 14 1110         1
# 15 1111         0


class number_complement(object):
    def solution1(self, num):
        a = 1
        while a < num:
            a <<= 1
        return a - 1 if a == num else a - num - 1

if __name__ == '__main__':
    pass