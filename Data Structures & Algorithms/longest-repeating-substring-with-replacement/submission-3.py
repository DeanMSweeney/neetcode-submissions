class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # two pointers 
        l, r = 0, 0
        freq = {}
        max_ss = 0
        rep = 0 
        while r <= len(s) - 1 and l <= r: 
            if rep <= k: 
                if s[r] in freq:
                    freq[s[r]] += 1
                else:
                    freq[s[r]] = 1

            max_c = max(freq.values())
            ss_len = (r - l) + 1
            rep = ss_len - max_c 

            if rep <= k:
                r += 1 
                max_ss = max(max_ss, ss_len)
            else:
                freq[s[l]] -= 1
                l += 1
        return max_ss 
            



        
        

                
        