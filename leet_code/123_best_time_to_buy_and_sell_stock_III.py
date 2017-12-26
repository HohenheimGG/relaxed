# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
#
# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

class BestTimeToBuyAndSellIII(object):
    def solution1(self, prices, n):
        gl = [0] * (n + 1)
        local = [0] * (n + 1)

        index = 0
        while index < len(prices) - 1:
            diff = prices[index + 1] - prices[index]
            for time in range(n, 0, -1):
                local[time] = max(gl[time - 1] + diff if diff > 0 else 0, local[time] + diff)
                gl[time] = max(gl[time], local[time])
            index += 1
        return gl[n]

if __name__ == '__main__':
    nums = [7, 1, 5, 3, 6, 4, 1, 9]
    # nums = [7, 6, 4, 3, 1]
    result = BestTimeToBuyAndSellIII().solution1(nums, 2)
    print result
