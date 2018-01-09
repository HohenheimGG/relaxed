#coding:utf-8
# You are given an array of positive and negative integers.
# If a number n at an index is positive, then move forward n steps.
# Conversely, if it’s negative (-n), move backward n steps.
# Assume the first element of the array is forward next to the last element,
# and the last element is backward next to the first element.
# Determine if there is a loop in this array.
# A loop starts and ends at a particular index with more than 1 element along the loop.
# The loop must be “forward” or “backward’.
#
# Example 1: Given the array [2, -1, 1, 2, 2], there is a loop, from index 0 -> 2 -> 3 -> 0.
#
# Example 2: Given the array [-1, 2], there is no loop.
#
# Note: The given array is guaranteed to contain no element “0”.
#
# Can you do it in O(n) time complexity and O(1) space complexity?

class CircularArrayLoop(object):
    def solution1(self, nums):
        size = len(nums)
        temp = {}
        visited = [False for n in range(0, size)]

        for i in range(0, size):
            if visited[i]:
                continue
            cur = i
            while True:
                visited[cur] = True
                next = (cur + nums[cur]) % size
                if next < 0:
                    cur = next + size
                if next == cur or nums[cur] * nums[next] < 0:
                    break
                if cur in temp:
                    return True
                temp[cur] = next
                cur = next

        return False

if __name__ == '__main__':
    result = [1, -1]
    print CircularArrayLoop().solution1(result)