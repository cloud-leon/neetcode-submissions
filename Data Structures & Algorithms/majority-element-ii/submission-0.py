class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        indicator = math.floor(len(nums)/3)
        res = []
        for num,count in Counter(nums).items():
            if count > indicator:
                res.append(num)

        return res