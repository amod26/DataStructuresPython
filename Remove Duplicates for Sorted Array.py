nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.


def removeDuplicates(nums):
    j = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[j]:
            j = j + 1
            nums[j] = nums[i]
    return j + 1


print(removeDuplicates(nums))
