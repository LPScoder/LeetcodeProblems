class Solution(object):
    def twoSum(self, nums, target):
        dic = {} #create dictionary 
    
        for i in range(len(nums)): # iterate through lst
            num = target - nums[i] #find num needed to satisfy condition
            if num in dic.keys(): # check if num has been seen previously
                return [i, dic[num]] # if seen, return
            dic[nums[i]] = i # if not seen append to dic