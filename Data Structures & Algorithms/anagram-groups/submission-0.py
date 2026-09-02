# Problemn #1 - Group anagrams 

class Solution:
    def groupAnagrams(self, strs):
        res = defaultdict(list)
        for s in strs: # iterate through N strings O(N)
            count = [0] * 26
            for ch in s: # iterate through M caharacters O(M)
                count[ord(ch) - ord('a')] += 1 # ord returns unicode representing a character 
            res[(tuple(count))].append(s)
        return list(res.values())

                 
        