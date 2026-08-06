class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        l,r = 0,0
        while l < len(s):
            r = l
            while s[r] != "#":
                r+=1
            size = int(s[l:r])
            word = s[r+1:r+size+1]
            res.append(word)
            l = r+size+1
        return res