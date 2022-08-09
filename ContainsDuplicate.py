class Solution(object):
    def containsDuplicate(self, nums): 
        dic = {} # create empty dictionary/hashtable
        for i, num in enumerate(nums): #for loop with counter
            if dic.has_key(num): #check if number has appeared previously
                return True
            else:
                dic[num] = i #if it hasn't add unique value to hash
        return False