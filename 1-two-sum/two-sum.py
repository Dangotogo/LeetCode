class Solution(object):
    def twoSum(self, nums, target):
        if not nums:
            return 0

        twoSum = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                twoSum = nums[i] + nums[j]
                if twoSum == target:
                    return i,j

        return 0
        