class Solution:
    def scoreOfString(self, s: str) -> int:
        seq_diff = [] # sequential diff array
        for i in range(len(s) - 1):
            i_ord, j_ord = ord(s[i]), ord(s[i + 1])
            seq_diff.append(abs(j_ord - i_ord)) # compute and append seq diff
        return sum(seq_diff)
            
        