class Solution(object):
    def maxProfit(self, prices):
        maxProf = 0 # maximum profit
        minVal = prices[0] #minimum intialized to first index
        for i in range(len(prices)): #run through list
            if prices[i] < minVal: #finding the smallest leftmost value
                minVal = prices[i] 
            elif prices[i] - minVal > maxProf: #checking if index - leftmost minimum is max difference
                maxProf = prices[i] - minVal
        return maxProf