class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        strcnt = {}
        maxf = 0
        l=0
        res = 0
        for r in range(len(s)):
            strcnt[s[r]] = 1 + strcnt.get(s[r],0) 
            maxf = max(maxf,strcnt[s[r]])
            while (((r-l+1) - maxf) > k):
                strcnt[s[l]] -=1
                l+=1
            res = max(res,r-l+1)
            
        return res