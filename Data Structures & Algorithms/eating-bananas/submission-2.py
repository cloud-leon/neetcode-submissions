class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l ,r = 1, max(piles)

        res = 0
        while l <= r :
            k = (l + r) // 2
            curcount = 0
            for p in piles:
                curcount += math.ceil(p/k)

            if curcount > h:
                l = k +1
            else:
                res = k
                r = k -1
        return res 