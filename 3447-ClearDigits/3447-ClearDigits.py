# Last updated: 1/12/2026, 3:13:25 PM
class Solution:
    def clearDigits(self, s: str) -> str:
        #9:56

        # ad93kd3
        #    *
        # [k]

        stack = []

        for c in s:
            if c.isdigit():
                stack.pop()
            else:
                stack.append(c)
        
        return ''.join(stack)
        
        
