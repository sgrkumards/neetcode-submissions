class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for idx , ele in enumerate(nums):
            comp = target - ele
            if comp in seen:
                return [seen[comp], idx]

            seen[ele] = idx 

        