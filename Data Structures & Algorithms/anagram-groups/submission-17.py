class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            count = [0] * 26
            for ltr in word:
                count[ord(ltr)-ord("a")] +=1
            count = tuple(count)
            if count in seen:
                seen[count].append(word)
            else:
                seen[count] = [word]
        return list(seen.values())