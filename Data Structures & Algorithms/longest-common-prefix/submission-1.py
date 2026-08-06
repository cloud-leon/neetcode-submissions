class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if not strs:
            return prefix
       

        n = min(len(s) for s in strs)
        for length in range(n):
            holdingprefix = strs[0][:length+1]
            for word in strs:
                if word[:length+1]!= holdingprefix:
                    return prefix
            prefix = holdingprefix
        return prefix