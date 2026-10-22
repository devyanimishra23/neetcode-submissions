class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        best=0
        right=0
        seen=set()
        while right<len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            best=max(best,right-left+1)
            right+=1
        return best
