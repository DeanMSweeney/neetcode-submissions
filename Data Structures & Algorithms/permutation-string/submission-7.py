class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # create mapping 
        map = {}
        for s in s1:
            if s in map: 
                map[s] += 1 
            else:
                map[s] = 1
        r = 0 
        map_curr = dict(map)

        p_string = []
        while r <= len(s2) - 1:
            ch = s2[r]
            if ch not in map:
                r += 1
                p_string = []
                map_curr = dict(map)
            elif ch in map_curr:
                if map_curr[ch] > 1:
                    map_curr[ch] -= 1
                else:
                    map_curr.pop(ch)
                p_string.append(ch)
                r += 1
            else:
                # ch is in s1 but exhausted in current window -> shrink from left
                while ch not in map_curr:
                    left_ch = p_string.pop(0)
                    map_curr[left_ch] = map_curr.get(left_ch, 0) + 1
                map_curr[ch] -= 1
                if map_curr[ch] == 0:
                    map_curr.pop(ch)
                p_string.append(ch)
                r += 1

            if "".join(sorted(p_string)) == "".join(sorted(s1)):
                return True 
        return False