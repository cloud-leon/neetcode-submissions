class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        maxp = 0
        minprice = prices[0]
        for price in prices:
            minprice = min(price,minprice)
            maxp = max(maxp,price-minprice)
        return maxp