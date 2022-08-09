class Solution(object):
    def findMin(self, nums):
        if nums[0] < nums[-1] or len(nums) == 1: return nums[0] # if lst length 1 or hasn't been rotated
        def binSearch(numbs): #create a binary seach alg
            if numbs[len(numbs)/2] < numbs[(len(numbs)/2) - 1]: #condition to find minimum
                return numbs[len(numbs)/2]
            elif len(numbs) == 1:
                return 1
            return binSearch(numbs[:len(numbs)/2]) * binSearch(numbs[len(numbs)/2:]) #recurse left and right halves
        return binSearch(nums)