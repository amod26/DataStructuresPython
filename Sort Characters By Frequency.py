# Sort Characters By Frequency

# Given a string, sort it in decreasing order based on the frequency of characters.


class Solution:
    def frequencySort(self, s: str) -> str:
        ls = list(s)  # converting the string to list
        dic = collections.Counter(ls)

        t = dic.most_common()  # sorting the counter by value, This method returns a tuple
        res = ''
        for (k, v) in t:  # iterate through the tuple
            for i in range(v):
                res += k  # add characters to string res by frequency
        return res
