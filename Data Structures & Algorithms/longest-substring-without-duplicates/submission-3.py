class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curset = set()
        l = 0
        longest = 0
        for r in range(len(s)):
            while s[r] in curset:
                curset.remove(s[l])
                l+=1
            longest = max(longest,r-l+1)
            curset.add(s[r])
        return longest
    