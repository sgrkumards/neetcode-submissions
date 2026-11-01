class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
            


# brute force pproach 

# Begin 
     
#     need a dict  to store the index and compliment of target and element of nums 

#     if that element if already in dict return index from dict and current index 


# end 
    
       

        