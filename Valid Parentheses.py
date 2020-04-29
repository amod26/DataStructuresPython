Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack,pairs = [],{"(":")","[":"]","{":"}"}

        for char in s:
            if char in pairs:
                stack.append(char)
            elif len(stack)<=0:
                return False
            elif char in pairs.values() and char!=pairs[stack.pop()]:
                return False
        return True if stack==[] else False
