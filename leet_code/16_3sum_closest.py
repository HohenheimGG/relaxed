# in S such that the sum is closest to a given number, target.
# Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
#     For example, given array S = {-1 2 1 -4}, and target = 1.
#
#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class three_sum_closest(object):
    def solution1(self, nums, target):
        size = len(nums)
        if not nums or size < 3:
            return -1
        nums.sort()

        if 3 * nums[0] > target:
            return nums[0] + nums[1] + nums[2]

        if 3 * nums[size - 1] < target:
            return nums[size - 1] + nums[size - 2] + nums[size - 3]

        bestNum = nums[0] + nums[1] + nums[2]
        for index in range(0, size):
            lo, hi = index + 1, size - 1
            while lo < hi:
                curNum = nums[index] + nums[lo] + nums[hi]
                if curNum > target:
                    hi -= 1
                elif curNum < target:
                    lo += 1
                else:
                    hi -= 1
                    lo += 1
                if abs(curNum - target) < abs(bestNum - target):
                    bestNum = curNum
        return bestNum

if __name__ == '__main__':
    pass
