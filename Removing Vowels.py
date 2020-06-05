# Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.


class Solution:
    def removeVowels(self, S: str) -> str:
        vowels = ('a', 'e', 'i', 'o', 'u')
        for x in S.lower():
            if x in vowels:
                S = S.replace(x, "")
        return S
