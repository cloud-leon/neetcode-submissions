class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramhold = defaultdict(list)

        for word in strs:
            key= [0] *26
            for ch in word:
                key[ord(ch)- ord("a")] +=1
            anagramhold[tuple(key)].append(word)
            
        return list(anagramhold.values())