class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mem = set()
        l = 0    
        max_cnt = 0 
       
        for r in range(len(s)): # iterate through sequence
            while s[r] in mem: # if character in set then remove it and all before 
                mem.remove(s[l])
                l += 1 
            mem.add(s[r]) # add to memory
            max_cnt = max(max_cnt, r - l + 1) # tally count 
        
        return max_cnt
        
            