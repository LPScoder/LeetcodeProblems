class Solution(object):
    def search(self, nums, target):
        def binSearch(numbs, start, targ): #binary search algorithm
            if len(numbs) == 1 and numbs[0] != targ: #if the list is size 1... check
                return -1
            elif numbs[len(numbs)/2] == targ: #if the number is found, return 
                return len(numbs)/2 + start
            elif len(numbs) == 2: #if the list is length two perform check
                if numbs[0] == targ:
                    return start
                elif numbs[1] == targ: 
                    return start + 1
                return -1
            else: 
                a = binSearch(numbs[:len(numbs)/2], start, targ) #recurse first half tracking index
                b = binSearch(numbs[len(numbs)/2 + 1:], len(numbs)/2 + 1 + start, targ) #recurse second half tracking index
                if(a > -1):
                    return a
                else:
                    return b
        
        return binSearch(nums, 0, target)