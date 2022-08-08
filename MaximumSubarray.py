class Solution(object):
    def maxSubArray(self, nums):
        
        currentMaxSum = 0
        finalMaxSum = nums[0]
        
        for i in nums:
            if currentMaxSum < 0:
                currentMaxSum = 0
            currentMaxSum += i
            finalMaxSum = max(finalMaxSum, currentMaxSum)
            
        return finalMaxSum