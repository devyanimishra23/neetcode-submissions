class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        need = {}                          # what t needs: letter → count
        for c in t:
            need[c] = need.get(c, 0) + 1

        window = {}                        # what the window has
        have = 0                           # letters whose count is fully met
        goal = len(need)                   # how many different letters must be met
        best_len = float("inf")
        best_start = 0
        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1                  # 1. grow
            if c in need and window[c] == need[c]:
                have += 1                                     #    this letter is now fully met

            while have == goal:                               # 2. window works → squeeze
                if right - left + 1 < best_len:               #    record before shrinking
                    best_len = right - left + 1
                    best_start = left
                d = s[left]
                window[d] -= 1                                #    drop the tail letter
                if d in need and window[d] < need[d]:
                    have -= 1                                 #    lost a needed letter
                left += 1

        if best_len == float("inf"):
            return ""
        return s[best_start : best_start + best_len]