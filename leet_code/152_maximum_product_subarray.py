# Find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.

class MaximunProductSubarray(object):
    def solution1(self, nums):
        if not nums:
            return [0]
        maxCache = [0 for i in range(len(nums))]
        minCache = [0 for i in range(len(nums))]

        maxCache[0] = minCache[0] = nums[0]
        result = nums[0]
        for index in range(1, len(nums)):
            maxCache[index] = minCache[index] = nums[index]
            if nums[index] > 0:
                maxCache[index] = max(maxCache[index], maxCache[i - 1] * nums[index])
                minCache[index] = min(minCache[index], minCache[i - 1] * nums[index])
            elif nums[index] < 0:
                maxCache[index] = max(maxCache[index], minCache[i - 1] * nums[index])
                minCache[index] = min(minCache[index], max[i - 1] * nums[index])
            result = max(result, maxCache[i])

        return result
