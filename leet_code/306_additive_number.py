# -*- coding: utf-8 -*-
# Additive number is a string whose digits can form additive sequence.
#
# A valid additive sequence should contain at least three numbers. Except for the first two numbers,
# each subsequent number in the sequence must be the sum of the preceding two.
#
# For example:
# “112358” is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
#
# 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# “199100199” is also an additive number, the additive sequence is: 1, 99, 100, 199.
# 1 + 99 = 100, 99 + 100 = 199
# Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.
#
# Given a string containing only digits ‘0’-‘9’, write a function to determine if it’s an additive number.
#
# Follow up:
# How would you handle overflow for very large input integers?

# 一次可以分多少个数字? 以位数区分, 先确认最大可分位数size
# 一次可分数字的大小不可以超过位数一半, 所以有最小可分位数3
# 分割数字时必须越来越大, 下个数字必须比上个数字大, 所以不是先切割数字, 而是在比较过程中切割
# 如何确认每次切割的位数?

import math

class AdditiveNumber(object):
    def solution1(self, num):
        size = len(num)
        result = []
        if size < 2:
            return result

        maxCount = (int)(math.floor(size / 2))

        for i in range(1, maxCount - 1):

            j = 1
            while j < max(maxCount - 1, size - i - j):
                first = num[0 : i]
                second = num[i : i + j]
                result.append(first)
                result.append(second)
                cur = i + j
                if not self.isValid(first) or not self.isValid(second):
                    j += 1
                    continue
                while cur < size:
                    expected = self.sum(first, second)
                    if len(expected) + cur > size:
                        break
                    if num[cur : len(expected) + cur] != expected:
                        break
                    first = second
                    second = expected
                    cur += len(expected)
                    result.append(expected)
                if cur == size:
                    return result
                result = []
                j += 1
        return result

    def isValid(self, s):
        return s[0:1] != '0'

    def sum(self, s1, s2):
        return str(int(s1) + int(s2))

if __name__ == '__main__':
    num = '199100199'
    result = AdditiveNumber().solution1(num)
    print result