# Given a binary array, find the maximum number of consecutive 1s in this array.


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = max_count = 0
        for nums in nums:
            if nums == 1:
                count += 1
            elif nums == 0:
                max_count = max(max_count, count)
                # Reset count of 1.
                count = 0
        return max(max_count, count)
