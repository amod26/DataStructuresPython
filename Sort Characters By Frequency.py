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
# Using Arrays & sorting
class Solution:
    def frequencySort(self, s: str) -> str:
        if not s:
            return s
        
        s=list(s)
        
        s.sort()
        
        all_strings=[]
        cur_sb= [s[0]]
        for c in s[1:]:
            if cur_sb[-1] != c:
                all_strings.append("".join(cur_sb))
                cur_sb=[]
            cur_sb.append(c)
        all_strings.append(''.join(cur_sb))
        
        all_strings.sort(key=lambda string:len(string),reverse=True)
        return "".join(all_strings)
    
    
  # Using Hashmap & sorting
def frequencySort(self, s: str) -> str:

    # Count up the occurances.
    counts = collections.Counter(s)
    
    # Build up the string builder.
    string_builder = []
    for letter, freq in counts.most_common():
        # letter * freq makes freq copies of letter.
        # e.g. "a" * 4 -> "aaaa"
        string_builder.append(letter * freq)
    return "".join(string_builder)
