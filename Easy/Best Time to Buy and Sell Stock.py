class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left = buy, right = sell
        l, r = 0, 1
        # set max profit to 0
        maxP = 0

        while r < len(prices):
            # compare the left point and right pointer
            if prices[l] < prices[r]:
                # dictate profit. subtract right from left
                profit = prices[r] - prices[l]
                # find the maximum, between current max profit and new profit instance
                maxP = max(maxP, profit)
            else:
                # incremetning slider, shift left pointer to right pos
                l = r
                # shift right pointer +1 (left pointer has taken its pos)
            r += 1
        return maxP