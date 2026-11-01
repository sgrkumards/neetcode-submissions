class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!= len(t):
            return False 

        countS , countT = {} ,{}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i],0)

        return countS == countT
        
       

# Begin 
#     defination of anagram is when both same and same frequency 

#     if length of both input string is not equal we can return False 
#     no need to check any further 

#     need dictory keep on ascount of charactes of string 

#     we loop thriugh with length of any onr of string 

#     kepp adding chr and freq in dict .

#     once all done if both frecount dict are equsal we will return True else false 

# end 