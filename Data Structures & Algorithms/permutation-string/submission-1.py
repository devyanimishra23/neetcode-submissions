class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if k > len(s2):
            return False

        need = {}                                   
        for c in s1:
            need[c] = need.get(c, 0) + 1

        window = {}                                
        for right in range(len(s2)):
            c = s2[right]
            window[c] = window.get(c, 0) + 1      

            if right >= k:                         
                out = s2[right - k]                
                window[out] -= 1
                if window[out] == 0:
                    del window[out]                

            if window == need:                     
                return True
        return False