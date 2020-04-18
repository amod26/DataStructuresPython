# Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.

nums = [23, 2, 6, 4, 7]
k = 6


def checkSubarraySum(nums, k):
    sums = [0] * (len(nums) + 1)
    d = {0: 0}
    for i in range(0, len(nums)):
        sums[i + 1] = sums[i] + nums[i]
        mod = sums[i + 1] % k if k != 0 else sums[i + 1]
        if mod in d:
            if i + 1 - d[mod] >= 2:
                return True
        else:
            d[mod] = i + 1
    return False


checkSubarraySum(nums, k)
