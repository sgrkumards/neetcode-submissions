class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parn_freq = {')':'(','}':'{',']':'['}
        for c in s:
            if c in parn_freq :
                if stack and stack[-1] == parn_freq[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
        