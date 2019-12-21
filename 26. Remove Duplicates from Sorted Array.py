class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
                i -= 1
            i += 1
        return len(nums)


try1 = Solution().removeDuplicates(nums=[0,0,1,1,1,2,2,3,3,4])
print(try1)



'''
Do not allocate extra space for another array, you must do this by modifying the input array
不允许再额外创建列表，必须在原有的输入列表上改动。
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #此题因为不允许开辟额外空间，所以不推荐使用删除重复元素。而选择将不重复元素放在原列表开头，返回新列表长度，截取原列表即可。
        if len(nums) == 0:
            return 0
        j = 0
        len_n = len(nums)
        for i in range(len_n):
            if nums[j] != nums[i]:
                nums[j + 1] = nums[i]
                j += 1
        return j + 1

'''
