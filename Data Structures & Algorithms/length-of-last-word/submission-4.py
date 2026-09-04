class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        rev = s[::-1] # reverse order in string 
        last_wrd = []
        ch = 0 

        if len(rev) == 1:
            return len(rev)

        while rev[ch] == " ":
            ch += 1
        
        while rev[ch] != " " and ch < len(rev) - 1:
            last_wrd.append(rev[ch])
            ch += 1
            
        return len(last_wrd)
             