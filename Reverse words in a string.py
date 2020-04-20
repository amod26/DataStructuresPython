class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        return " ".join(arr[::-1])
