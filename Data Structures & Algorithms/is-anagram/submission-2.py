class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        charHash = [0] * 26

        for i in range(len(s)):
            charHash[ord(s[i])- ord('a')] += 1
            charHash[ord(t[i]) - ord('a')] -= 1

        for val in charHash:
            if val != 0 :
                return False 
        
        return True 
