class Solution(object):
    def maxSubArray(self, nums):
        currentMaxSum = 0
        finalMaxSum = nums[0] #intialize
        for i in nums: #move through nums
            if currentMaxSum < 0: #reset window if dips below 0
                currentMaxSum = 0
            currentMaxSum += i #add ned value
            finalMaxSum = max(finalMaxSum, currentMaxSum) #checker!
        return finalMaxSum