class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for word in strs:
            counter = [0] * 26

            for ch in word:
                counter[ord(ch) - ord("a")] +=1
            cntr = tuple(counter)
            if cntr in seen:
                seen[cntr].append(word)
            else:
                seen[cntr] = [word]

        return list(seen.values())
