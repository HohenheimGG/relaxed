# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.

class MaximumSubarray:
    def solution1(self, nums):
        if not nums:
            return None
        length = len(nums)
        start = 0
        end = 0
        max = None
        for i in range(0, length):
            j = i
            sum = 0
            while j < length:
                sum += nums[j]
                if max is None or sum > max:
                    max = sum
                    start = i
                    end = j
                j += 1

        result = []
        for k in range(start, end + 1):
            result.append(nums[k])
        return result

if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = MaximumSubarray().solution1(nums)
    print result

