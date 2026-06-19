class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        m = len(nums)
        ans = [0] * (2*m)
        for i,n in enumerate(nums):
            ans[i] = ans[i+m] = n 
        return ans  