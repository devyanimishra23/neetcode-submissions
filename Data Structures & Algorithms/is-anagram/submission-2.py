class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count_s={}
        count_t={}
        for ch in s:
            count_s[ch]=count_s.get(ch,0)+1
        for i in t:
            count_t[i]=count_t.get(i,0)+1
        
        return count_t==count_s
