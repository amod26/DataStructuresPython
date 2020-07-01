class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [nums[i]+sum(nums[0:i])  for i in range(len(nums))]