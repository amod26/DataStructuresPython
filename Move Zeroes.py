nums = [0, 2, 0, 1, 0, 3, 12]

# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.


def moveZeroes(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums


print(moveZeroes(nums))
