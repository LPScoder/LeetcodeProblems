class Solution(object):
    def maxProfit(self, prices):
        maxProf = 0
        minVal = prices[0]
        for i in range(len(prices)):
            if prices[i] < minVal:
                minVal = prices[i]
            elif prices[i] - minVal > maxProf:
                maxProf = prices[i] - minVal
        return maxProf