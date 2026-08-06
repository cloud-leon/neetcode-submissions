class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)

        for word in strs:
            wordcount = [0] * 26
            for c in word:
                wordcount[ ord(c) - ord("a")] +=1
            anagramMap[tuple(wordcount)].append(word)
        

        return list(anagramMap.values())