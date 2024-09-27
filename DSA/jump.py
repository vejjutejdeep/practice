class Solution:

    def canJump(self, nums):
        # print(nums)
        pos = 0
        i = 1
        if len(nums) <= 1:
            return True
        while i <= nums[pos]:
            print(i, nums)
            pos += i
            # print("position",pos)
            temp = nums[pos:]
            i += 1 
            # return self.canJump(temp)
        return False
    
Solution = Solution()
print(Solution.canJump([2,3,1,1,4]))
print(Solution.canJump([3,2,1,0,4]))
print(Solution.canJump([0]))
print(Solution.canJump([2,0,0]))