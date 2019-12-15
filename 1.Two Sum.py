# Given nums = [2, 7, 11, 15], target = 9


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_dict = {}
        for i in range(len(nums)):
            if nums[i] in hash_dict:
                return [hash_dict[nums[i]], i]
            else:
                hash_dict[target - nums[i]] = i


# d[7]=0
# d[2]=1
