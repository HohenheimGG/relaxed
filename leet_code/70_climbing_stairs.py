# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Note: Given n will be a positive integer.
#
#
# Example 1:
#
# Input: 2
# Output:  2
# Explanation:  There are two ways to climb to the top.
#
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:
#
# Input: 3
# Output:  3
# Explanation:  There are three ways to climb to the top.
#
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

class ClimbingStairs(object):
    def solution1(self, n):
        if n == 0:
            return 0
        result = []
        self.recursive(n, result, "")
        return result

    def recursive(self, n, result, temp):
        if n == 0:
            result.append(temp[0:len(temp) - 3])
            return
        if n >= 2:
            self.recursive(n - 2, result, temp + "2 step + ")
            self.recursive(n - 1, result, temp + "1 step + ")
        else:
            self.recursive(n - 1, result, temp + "1 step + ")

if __name__ == '__main__':
    result = ClimbingStairs().solution1(4)
    print result
