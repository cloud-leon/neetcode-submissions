class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        checkset = set()
        candidates.sort()

        def backtrack(i, hold,total):
            if total == target:
                if tuple(hold) not in checkset:
                    res.append(hold.copy())
                    checkset.add(tuple(hold.copy()))
                    return
                
            if total > target or i == len(candidates):
                return
            hold.append(candidates[i])
            backtrack(i+1,hold,total + candidates[i])
            hold.pop()
            backtrack(i+1,hold,total)
        backtrack(0,[],0)
        return res


