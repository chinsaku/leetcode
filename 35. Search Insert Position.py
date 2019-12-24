class Solution:
    def searchInsert(self, nums, target: int) -> int:
        for i in range(len(nums)):
            if nums[i]>=target:
                return i
        
        return i+1
        

try1 = Solution().searchInsert([1,3,5,6],5)
print(try1)