class Solution(object): # need to update to make shorter
    def maxProduct(self, nums):
        oneVal = 1 # set up two trackers... one that will be negative
        twoVal = None # while the other value will be positive and they will alternate
        finalVal = None #this will track the final maximum product
        holder = 0 # this will be used as a flag for when to initialize the seond value
        for i in nums: # one loop
            if i == 0: # if lst value is 0 reset
                oneVal = 1
                twoVal = None
                finalVal = max(finalVal, 0) #check if zero is largest
                holder = 0 #reset holder
            else:
                if oneVal < 0: #for first negative
                    holder += 1
                    if holder == 1: #only first negative
                        twoVal = 1 #initialize second tracker
                if holder:
                    twoVal *= i 
                oneVal *= i
                finalVal = max(oneVal, twoVal, finalVal) #final check
        return finalVal