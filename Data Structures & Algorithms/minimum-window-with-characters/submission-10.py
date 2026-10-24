class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
    
        need={}
        for c in t:
            need[c]=need.get(c,0)+1
        
        window={}
        left=0
        best_len=float('inf')
        best_start=0
        have,goal=0,len(need)

        for right in range(len(s)):
            c=s[right]
            window[c]=window.get(c,0)+1
            if c in need and window[c]==need[c]:
                have+=1
            while have==goal:
                if right-left+1<best_len:
                    best_len=right-left+1
                    best_start=left
                d=s[left]
                window[d]-=1
                if d in need and window[d]<need[d]:
                    have-=1
                left+=1
            
        if best_len==float("inf"):
                return''
        return s[best_start:best_start+best_len]
        