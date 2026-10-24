class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if k > len(s2):
            return False

        need = {}                                   # counts of s1
        for c in s1:
            need[c] = need.get(c, 0) + 1

        window = {}                                 # counts of the current window
        for right in range(len(s2)):
            c = s2[right]
            window[c] = window.get(c, 0) + 1        # letter comes in

            if right >= k:                          # window is one too big
                out = s2[right - k]                 # the letter falling out
                window[out] -= 1
                if window[out] == 0:
                    del window[out]                 # remove empty keys

            if window == need:                      # same letters, same amounts
                return True
        return False