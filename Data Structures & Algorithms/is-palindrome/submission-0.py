class Solution:
    def isPalindrome(self, s: str) -> bool:

        l = 0 # left pointer 
        r = len(s) - 1 # right pointer 
        while l < r: 
            while l < r and not self.alpn(s[l]):
                l += 1 # move right
            while l < r and not self.alpn(s[r]): 
                r -= 1 # move left 
            if s[l].lower() != s[r].lower():
                return False 
            l += 1 
            r -= 1

        return True 

    def alpn(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))


        

        
        