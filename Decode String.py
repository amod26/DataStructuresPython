# Decode String
# Given an encoded string, return its decoded string.
# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in s:
            if i != ']':
                stack.append(i)
                continue
            tmp = ''
            while stack and stack[-1] != '[':
                tmp = stack.pop() + tmp
            stack.pop()
            num = ''
            while stack and stack[-1].isnumeric():
                num = stack.pop() + num
            stack.append(int(num) * tmp)

        return ''.join(stack)
