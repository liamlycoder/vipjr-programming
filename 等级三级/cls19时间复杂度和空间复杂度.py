"""
作业：LeetCode第一题
"""
nums = [2, 7, 11, 15]
target = 9

"""
时间复杂度：O（n**2)
空间复杂度：O（1）
"""
def twoSum(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    else:
        return []

"""
时间复杂度：O（n)
空间复杂度：O（n）
"""
def twoSum2(nums, target):
    dct = {}
    for ind, num in enumerate(nums):
        num2 = target - num
        if num2 in dct:
            return [dct[num2], ind]
        dct[num] = ind
    return []

print(twoSum2(nums, target))
