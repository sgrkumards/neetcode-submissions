from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevHash = defaultdict(int)
        for i, n in enumerate(nums):
            comp = target - n 
            if comp in prevHash:
                return [prevHash[comp], i]
            prevHash[n] = i
  
       